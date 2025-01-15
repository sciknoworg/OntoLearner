
import os
import logging
from dotenv import load_dotenv

from langchain_core.prompts        import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_cerebras            import ChatCerebras
from langchain_openai import ChatOpenAI

from ontolearner.utils.utils import load_dataset

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

llama_model = ChatCerebras(
    cerebras_api_key = os.getenv('CEREBRAS_API_KEY'),
    model            = "llama-3.3-70b",
    max_tokens       = 100,
    temperature      = 0,
)

intent_model = ChatOpenAI(
    openai_api_key = os.getenv('OPENAI_API_KEY'),
    model_name     = "gpt-4o",
    max_tokens     = 100,
    temperature    = 0,
)

typing_template = """
In the domain of {domain}, what type the term {term} is?

Output a JSON object:
    {{
        "term": "{term}",
        "type": "type",
        "reasoning": "Explain why you think this term is of this type."
    }}
"""

typing_prompt: PromptTemplate = PromptTemplate(
    template=typing_template,
    input_variables=[
        "term",
        "domain"
    ]
)

intent_chain = typing_prompt | intent_model | JsonOutputParser()


def evaluate_term_typing(llm, test_data, limit=2):
    correct = 0
    index = 0
    total = len(test_data)

    for example in test_data:
        prediction = intent_chain.invoke(
            {
                "term": example['term'],
                "domain": "computer science"
            }
        )

        logger.info(f"Term: {example['term']}, Type: {example['type']}, Prediction: {prediction}")

        if prediction.get('type', '') == example['type'].lower():
            correct += 1

        logger.info(f"Term: {example['term']}, Type: {example['type']}, Prediction: {prediction}")

        index += 1
        if index >= limit:
            break

    accuracy = correct / total

    return accuracy


# Load the test dataset
test_dataset = load_dataset("../../data/datasets/train_typing_dataset.json")

# Evaluate the LLM on the test data
llm_accuracy = evaluate_term_typing(llama_model, test_dataset)

logger.info(f"LLM accuracy: {llm_accuracy}")
