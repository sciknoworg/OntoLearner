import logging
import os
from pathlib import Path
import pandas as pd
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import login

from ontolearner import Learner
from ontolearner.data_structure import OntologyData
from ontolearner.evaluation.metrics import calculate_term_typing_metrics
from ontolearner.evaluation.evaluate import aggregate_metrics
from ontolearner.evaluation.visualisations import (plot_model_comparison, plot_type_analysis,
                                                   plot_precision_recall_distribution)
from ontolearner.learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner
from ontolearner.learner.prompt import StandardizedPrompting
from ontolearner.ontology import Wine, MGED, AFO, PROCO, VIBSO, ENVO, SWEET
from ontolearner.utils.train_test_split import train_test_split

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

_ = load_dotenv(find_dotenv())
huggingface_token = os.environ.get('HUGGINGFACE_ACCESS_TOKEN')
login(token=huggingface_token)

DATA_DIR = Path("../data")
ONTOLOGIES_DIR = DATA_DIR / "ontologies"
METRICS_DIR = DATA_DIR / "metrics"

ontologies4learning = [
    Wine(),
    MGED(),
    AFO(),
    PROCO(),
    VIBSO(),
    ENVO(),
    SWEET()
]


llm_models = [
    "Qwen/Qwen3-0.6B",
    # "deepseek-ai/deepseek-llm-7b-chat",
    "deepseek-ai/deepseek-llm-7b-base",
    "meta-llama/Llama-3.1-8B-Instruct",
    "mistralai/Mistral-7B-Instruct-v0.1"
]

retriever_models = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "google/flan-t5-base",
    # "nomic-ai/nomic-embed-text-v1.5",
    # "ngram-embeddings"
]


def evaluate_term_typings_model_performance(train_data, test_data, llm_id, retriever_id, top_k=1):
    """Evaluate performance of a specific model configuration"""
    retriever = BERTRetrieverLearner()
    llm = AutoLearnerLLM(token=huggingface_token)
    prompting = StandardizedPrompting(task="term-typing")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    learner.learn(
        train_data,
        task="term-typing",
        retriever_id=retriever_id,
        llm_id=llm_id,
        top_k=top_k
    )

    results = []
    for typing in test_data.term_typings:
        raw_term = typing.term
        ground_truth = typing.types
        predicted = rag_learner.predict(raw_term, task="term-typing")

        metrics = calculate_term_typing_metrics(predicted, ground_truth)

        results.append({
            'term': raw_term,
            'ground_truth': ground_truth,
            'predicted': predicted,
            **metrics
        })

        logger.info("-" * 50)
        logger.info(f"Term: {raw_term}")
        logger.info(f"Ground Truth: {ground_truth}")
        logger.info(f"Predicted: {predicted}")
        logger.info(f"F1 Score: {metrics['f1_score']:.4f}")
        logger.info("-" * 50)

    agg_metrics = aggregate_metrics(results, "term-typing")

    # Add model information
    model_info = {
        'llm': llm_id,
        'retriever': retriever_id,
        'top_k': top_k
    }

    eval_results = {
        'model_info': model_info,
        'detailed_results': results,
        'aggregated_metrics': agg_metrics
    }

    return eval_results


def run_model_comparison():
    """Run comparison across multiple models"""
    ontology = ontologies4learning[0]
    ontology_domain = ontology.domain.lower().replace(' ', '_')
    ontology_path = ONTOLOGIES_DIR / ontology_domain / f"{ontology.ontology_id.lower()}.{ontology.format.lower()}"
    ontology.load(str(ontology_path))
    data: OntologyData = ontology.extract()

    if not data.term_typings:
        logger.warning(f"No term typings found in the {ontology.ontology_id} ontology data!")
        return

    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    logger.info(f"Created train/test split: {len(train_data.term_typings)} train, {len(test_data.term_typings)} test")

    all_results = []
    for llm_id in llm_models:
        for retriever_id in retriever_models:
            logger.info(f"Testing configuration: LLM={llm_id}, Retriever={retriever_id}")

            eval_result = evaluate_term_typings_model_performance(
                train_data=train_data,
                test_data=test_data,
                llm_id=llm_id,
                retriever_id=retriever_id
            )

            if eval_result:
                all_results.append({
                    'llm': llm_id,
                    'retriever': retriever_id,
                    'metrics': eval_result['aggregated_metrics'],
                    'detailed_results': eval_result['detailed_results']
                })

    if all_results:
        # Create summary dataframe
        summary_rows = []
        for result in all_results:
            summary_rows.append({
                'LLM Model': result['llm'],
                'Retriever Model': result['retriever'],
                'Precision Score': result['metrics']['avg_precision_score'],
                'Recall Score': result['metrics']['avg_recall_score'],
                'F1 Score': result['metrics']['avg_f1_score'],
                'Exact Match': result['metrics']['avg_exact_match']
            })

        summary_df = pd.DataFrame(summary_rows)
        summary_df.to_csv(METRICS_DIR / "model_metrics.csv", index=False)
        logger.info(f"Results saved to {METRICS_DIR / 'model_metrics.csv'}")

        # Find best model by F1 score
        best_idx = summary_df['F1 Score'].idxmax()
        best_model = summary_df.iloc[best_idx]

        logger.info("Best model configuration:")
        logger.info(f"LLM: {best_model['LLM Model']}")
        logger.info(f"Retriever: {best_model['Retriever Model']}")
        logger.info(f"F1 Score: {best_model['F1 Score']:.4f}")

        plot_model_comparison(summary_df, METRICS_DIR)
        plot_precision_recall_distribution(all_results, METRICS_DIR)
        plot_type_analysis(all_results, METRICS_DIR)


if __name__ == "__main__":
    run_model_comparison()

    # # Testing taxonomy discovery predictions
    # for tax_rel in data.type_taxonomies.taxonomies[:5]:
    #     raw_input = (tax_rel.parent, tax_rel.child)
    #     prediction = rag_learner.predict(raw_input, task="taxonomy-discovery")
    #     logger.info(f"Parent: {raw_input[0]}\n"
    #                 f"Child: {raw_input[1]}\n"
    #                 f"Predicted: {prediction}")
    #
    # # Testing non-taxonomy discovery predictions
    # for non_tax_rel in data.type_non_taxonomic_relations.non_taxonomies[:5]:
    #     raw_input = (non_tax_rel.head, non_tax_rel.tail)
    #     prediction = rag_learner.predict(raw_input, task="non-taxonomy-discovery")
    #     logger.info(f"Head: {raw_input[0]}\n"
    #                 f"Tail: {raw_input[1]}\n"
    #                 f"Predicted: {prediction}")
