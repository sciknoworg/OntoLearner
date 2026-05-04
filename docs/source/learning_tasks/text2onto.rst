Text2Onto
==================================

Data Generator
-----------------------------------------
OntoLearner library can be used to generate synthetic data for evaluating the task of term and type extraction from natural language text. It will generate a text corpus of documents aligned with a given ontology.

The first step is to load the ontology data from the selected ontology.

.. code-block:: python

    from ontolearner.ontology import ConferenceOntology

    conference = ConferenceOntology()
    conference.load()
    ontological_data = conference.extract()

    print(f"term types: {len(ontological_data.term_typings)}")
    print(f"taxonomic relations: {len(ontological_data.type_taxonomies.taxonomies)}")
    print(f"non-taxonomic relations: {len(ontological_data.type_non_taxonomic_relations.non_taxonomies)}")


As the second step, an LLM is used to generate synthetic text documents. Text2Onto now uses a direct ``transformers`` backend for generation, so you can run it with a Hugging Face model locally or with a remote model that is accessible through the standard Transformers APIs.

The generator also enriches the prompt with ontology-aware context derived from the extracted term typing, taxonomy, and non-taxonomic relation structure. This improves faithfulness and helps the model produce more coherent passages that stay closer to the source ontology.

.. note::

     Text2Onto works best with instruction-tuned Hugging Face models that can follow structured-output prompts. Smaller models can work for quick demos, while stronger instruction-tuned models usually produce cleaner passages and more consistent JSON.

You can configure the generator directly with a model identifier, optional Hugging Face token, and decoding settings.

.. code-block:: python

    from dotenv import load_dotenv
    import os

    from ontolearner.text2onto import SyntheticGenerator

    load_dotenv(override=True)

    pseudo_sentence_batch_size = 50
    max_worker_count_for_llm_calls = 3
    text2onto_synthetic_generator = SyntheticGenerator(batch_size=pseudo_sentence_batch_size,
                                                        worker_count=max_worker_count_for_llm_calls,
                                                        model_id=os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct"),
                                                        token=os.getenv("HF_TOKEN", ""),
                                                        device=os.getenv("TEXT2ONTO_DEVICE", "auto"),
                                                        max_new_tokens=256)
    synthetic_data = text2onto_synthetic_generator.generate(ontological_data=ontological_data,
                                                                    topic=ontology.domain)

.. tip::

   For better generation quality, use an instruction-tuned model, keep temperature low, and increase ``batch_size`` only when the ontology context still fits comfortably into the model context window.

.. note::

   The generator does not rely on DSPy anymore. If you previously configured DSPy for Text2Onto, you can remove that setup and pass the model directly through ``SyntheticGenerator``.

Data Splitter
------------------------

You can split the generated synthetic data for training, hyperparameter optimization (validation), and testing purposes.

If you want to improve the synthetic corpus further, the current generator can be extended with:

* richer ontology context retrieval from neighboring terms or parent chains,
* stricter JSON/structured-output validation,
* post-generation repair retries when required labels are missing,
* and optional reranking of multiple candidate passages.

.. code-block:: python

    from ontolearner.text2onto import SyntheticDataSplitter

    splitter = SyntheticDataSplitter(synthetic_data=synthetic_data, onto_name=ontology.ontology_id)
    terms, types, docs, types2docs = splitter.split(train=0.8, val=0.1, test=0.1)
