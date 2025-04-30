import dspy
import os
from dotenv import load_dotenv

from ontolearner.ontology import OM
from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter


load_dotenv(override=True)

# configure LLM for DSPy with LiteLLM - https://docs.litellm.ai/docs/providers
dspy_llm = dspy.LM(
    model=os.environ["LLM_MODEL_ID"],
    cache=True,
    max_tokens=4000,
    temperature=0,
    api_key=os.environ["LLM_API_KEY"],
    base_url=os.environ["LLM_BASE_URL"])
dspy.configure(lm=dspy_llm)

pseudo_sentence_batch_size = 50
max_worker_count_for_llm_calls = 3
text2onto_synthetic_generator = SyntheticGenerator(batch_size=pseudo_sentence_batch_size,
                                                   worker_count=max_worker_count_for_llm_calls)

ontology = OM()
ontology_path = "../data/om-2.0.rdf"
ontology.load(ontology_path)
ontological_data = ontology.extract()
print(f"term types: {len(ontological_data.term_types)}")
print(f"taxonomic relations: {len(ontological_data.taxonomic_relations.taxonomies)}")
print(f"non-taxonomic relations: {len(ontological_data.non_taxonomic_relations.non_taxonomies)}")

synthetic_data = text2onto_synthetic_generator.generate(ontological_data=ontological_data,
                                                                  topic=ontology.domain)

splitter = SyntheticDataSplitter(synthetic_data=synthetic_data, onto_name=ontology.ontology_id)

terms, types, docs, types2docs = splitter.split(train=0.8, val=0.1, test=0.1)
