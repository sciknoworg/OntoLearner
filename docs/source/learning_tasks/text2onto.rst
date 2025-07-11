Text2Onto
==================================

The Text2Onto task aims for **extracting ontological terminologies and types from a raw text**. So, for given an unstructured text corpus/documents, the goal is to identify foundational elements for ontology construction by recognizing domain-relevant vocabulary and categorizing it appropriately.

We aim to extract:

* **Terms (or Entities)**: These are specific terms that form the basis of an ontology. They populate the ontology by instantiating the defined classes. For instance, COVID-19 is a term of the type Disease, and Paris is a term of the type City.
* **Types (or Classes)**: These are abstract categories or groupings that represent general concepts within a domain. They form the backbone of an ontology's structure. Examples include Disease, Vehicle, or City.

By identifying and extracting these elements, the task helps bridge the gap between unstructured natural language and structured ontological knowledge. This process is critical for building knowledge representations that support reasoning, semantic integration, and advanced information retrieval.

To construct datasets for this task, OntoLearner leverages a **Synthetic Data Generator** module.


Data Generator
-----------------------------------------
OntoLearner library can be used to generate synthatic data for evaluating the task of term and type extraction from natural language text. It will generate a text corpus of documents aligned with a given ontology.

The first step is to load the ontology data from the selected ontology.

.. code-block:: python

    from ontolearner.ontology import ConferenceOntology

    conference = ConferenceOntology()
    conference.load()
    ontological_data = ontology.extract()

    print(f"term types: {len(ontological_data.term_typings)}")
    print(f"taxonomic relations: {len(ontological_data.type_taxonomies.taxonomies)}")
    print(f"non-taxonomic relations: {len(ontological_data.type_non_taxonomic_relations.non_taxonomies)}")


As the second step, an LLM is used to generate synthetic text documents. DSPy is used to connect to the LLM and parse the LLM outputs. You can use an LLM from an external provider
or host an LLM locally using tools such as Ollama or vLLM.

.. note::

     More details about all provides supported by ``DSPy`` (through *LiteLLM*) can be found in `this link <https://docs.litellm.ai/docs/providers>`_.

Information about the LLM is provided in a ``.env`` file similar to the following.

.. code-block::

    "LLM_MODEL_ID"={model_id_from_provider}
    "LLM_BASE_URL"={llm_provider_base_url}
    "LLM_API_KEY"={api_key_for_the_provider}


Then you can configure DSPy to use the provided LLM and generate the synthetic text documents using the ontology data extracted before.

.. code-block:: python

    from dotenv import load_dotenv
    import dspy

    from ontolearner.text2onto import SyntheticGenerator

    load_dotenv(override=True)

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
    synthetic_data = text2onto_synthetic_generator.generate(ontological_data=ontological_data,
                                                                    topic=ontology.domain)

Synthetic Data Splitter
------------------------

You can split the generated synthetic data using for training, hyperparameter optimization (validation), and testing purposes.

.. code-block:: python

    from ontolearner.text2onto import SyntheticDataSplitter

    splitter = SyntheticDataSplitter(synthetic_data=synthetic_data, onto_name=ontology.ontology_id)
    terms, types, docs, types2docs = splitter.split(train=0.8, val=0.1, test=0.1)
