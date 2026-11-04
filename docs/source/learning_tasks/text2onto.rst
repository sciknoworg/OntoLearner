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



Primitive Ontology Datasets
---------------------------

Text2Onto provides two variants for learning ontology relations from generated documents:

* **Ontology construction** predicts a complete set of ontology triples from a document.
* **Ontology expansion** predicts additional triples given a document and an initial ontology.

``SyntheticDataPreprocessor`` creates the common records used by both variants.
It matches generated documents to their pseudo-sentences, extracts ``is-a`` and
``instance-of`` triples, adds applicable non-taxonomic relations, and supports
LLM-based text cleaning, triple normalization, and alignment filtering.

Preprocessing
~~~~~~~~~~~~~

First generate training and test documents from their respective ontology splits,
then preprocess both using the same configuration:

.. code-block:: python

    import os
    from openai import OpenAI
    from ontolearner import train_test_split
    from ontolearner.ontology import OM
    from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

    ontology = OM()
    ontology.load()
    train_ontology, test_ontology = train_test_split(
        ontology.extract(), test_size=0.2, random_state=42
    )

    generator = SyntheticGenerator(
        model_id=os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct"),
        token=os.getenv("HF_TOKEN", ""),
        extraction_method="openai",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_model="gpt-4o-mini",
    )

    train_synthetic = generator.generate(ontological_data=train_ontology, topic=ontology.domain)
    test_synthetic = generator.generate(ontological_data=test_ontology, topic=ontology.domain)

    preprocessor = SyntheticDataPreprocessor(
        client=OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
        clean_text=True,
        deep_clean=True,
        alignment_filter=True,
    )
    train_records = preprocessor.preprocess(train_synthetic, train_ontology)
    test_records = preprocessor.preprocess(test_synthetic, test_ontology)

A preprocessed record contains its document text (``context``), extracted
``terms`` and ``types``, and the ground-truth ``primitive-ontology-triples``.
Alignment filtering keeps records whose text sufficiently supports the triples.

Ontology Construction
~~~~~~~~~~~~~~~~~~~~~

For construction, each record contains the document and its complete ontology.
The dataset fields are ``id``, ``context``, ``terms``, ``types``, and
``primitive-ontology-triples``. The triples are the prediction target.

.. code-block:: python

    from ontolearner.text2onto import PrimitiveOntologyDataset

    construction = PrimitiveOntologyDataset(task="ontology_construction")
    train_construction = construction.prepare(train_records)
    test_construction = construction.prepare(test_records)

Ontology Expansion
~~~~~~~~~~~~~~~~~~

For expansion, each record's triples are grouped by their object (tail), then
split into an initial ontology and triples to be predicted. At least one triple
per group remains in the initial ontology. ``terms`` and ``types`` identify
entities involved in the extension.

The dataset contains ``id``, ``context``, ``terms``, ``types``,
``initial-primitive-ontology-triples``, and
``extended-primitive-ontology-triples``. Records with no extension triples are
skipped.

.. code-block:: python

    expansion = PrimitiveOntologyDataset(task="ontology_expansion", random_state=42)
    train_expansion = expansion.prepare(train_records)
    test_expansion = expansion.prepare(test_records)

Both variants use the supplied training and test records, with gold triples
retained for evaluation. During prediction, the learner uses the task inputs
and the evaluator compares its predictions with the gold triples.
