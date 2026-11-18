Text2Onto
=========

The OntoLearner library can be used to generate synthetic data for evaluating
the task of term and type extraction from natural language text. It generates
a text corpus of documents aligned with a given ontology.

In addition to term and type extraction, Text2Onto supports synthetic data
generation for two other ontology learning tasks: **ontology construction**
and **ontology expansion**. Ontology construction involves generating datasets
for learning a complete primitive ontology from text, including terms, types,
and their relationships. Ontology expansion involves generating datasets for
extending an existing primitive ontology with additional concepts and
relationships extracted from text.

All three tasks share the same synthetic document generation process. Text2Onto
first generates natural-language documents aligned with an existing ontology.
The generated documents are then prepared for term and type extraction, ontology
construction, or ontology expansion according to the intended learning task.

The following sections first demonstrate this shared generation process,
followed by the task-specific preparation steps.

Data Generator
--------------

Load an ontology and extract its structured term, taxonomy and relation data.
The Conference ontology is used for this introduction.

.. code-block:: python

    from ontolearner.ontology import ConferenceOntology

    ontology = ConferenceOntology()
    ontology.load()
    ontological_data = ontology.extract()

    print("term types:", len(ontological_data.term_typings))
    print("taxonomic relations:", len(ontological_data.type_taxonomies.taxonomies))
    print("non-taxonomic relations:", len(
        ontological_data.type_non_taxonomic_relations.non_taxonomies
    ))

As a second step, an LLM generates synthetic text documents using a direct
``transformers`` backend. The generator enriches its prompts with context
derived from term typing, taxonomic and non-taxonomic relationships in the
selected ontology.

.. code-block:: python

    import os
    from dotenv import load_dotenv
    from ontolearner.text2onto import SyntheticGenerator

    load_dotenv(override=True)

    generator = SyntheticGenerator(
        batch_size=50,  # Pseudo-sentences per generation batch
        worker_count=3,  # Parallel generation workers
        model_id=os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct"),
        token=os.getenv("HF_TOKEN", ""),  # Optional Hugging Face token
        device=os.getenv("TEXT2ONTO_DEVICE", "auto"),
        max_new_tokens=256,  # Maximum tokens per generated passage
    )
    synthetic_data = generator.generate(
        ontological_data=ontological_data,
        topic=ontology.domain,
    )

.. note::

   Text2Onto works best with instruction-tuned Hugging Face models that can
   follow structured-output prompts. Smaller models can work for quick demos,
   while stronger instruction-tuned models usually produce cleaner passages
   and more consistent JSON.

.. tip::

   For better generation quality, use an instruction-tuned model, keep
   temperature low, and increase ``batch_size`` only when the ontology context
   still fits comfortably into the model context window.

.. note::

   The generator does not rely on DSPy anymore. If you previously configured
   DSPy for Text2Onto, you can remove that setup and pass the model directly
   through ``SyntheticGenerator``.

Data Preparation
----------------

After generating synthetic documents, prepare the data for the intended
ontology learning task. The term/type extraction workflow splits the
generated corpus, while construction and expansion preprocess the
documents into ontology-triple prediction samples.

Term and Type Extraction
~~~~~~~~~~~~~~~~~~~~~~~~

Use ``SyntheticDataSplitter`` to prepare training, validation and test data
for identifying terms and types in generated documents. It consumes the
``SyntheticGenerator`` output and returns three split dictionaries. Each
dictionary has keys
``docs``, ``terms``, ``types``, ``terms2docs`` and ``terms2types``.

.. code-block:: python

    from ontolearner.text2onto import SyntheticDataSplitter

    splitter = SyntheticDataSplitter(
        synthetic_data=synthetic_data,
        onto_name=ontology.ontology_id,
    )
    train_data, val_data, test_data = splitter.train_test_val_split(
        train=0.8, val=0.1, test=0.1  # Split proportions
    )

    print("train documents:", len(train_data["docs"]))
    print("validation documents:", len(val_data["docs"]))
    print("test documents:", len(test_data["docs"]))

Ontology Construction and Expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For ontology construction and expansion, ``SyntheticDataPreprocessor``
prepares ontology-triple prediction samples from synthetic documents and
their corresponding ontology data. Both use the same generation and
preprocessing process; the selected ``task`` determines whether each
sample contains a complete target ontology or an initial ontology with
additional triples to predict.

In the example below, split the source ontology first and then generate
documents for each partition to keep training and test data separate.

.. code-block:: python

    import os
    from dotenv import load_dotenv
    from openai import OpenAI
    from ontolearner import train_test_split
    from ontolearner.ontology import OM
    from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

    load_dotenv(override=True)

    ontology = OM()
    ontology.load()
    train_ontology, test_ontology = train_test_split(
        ontology.extract(), test_size=0.2, random_state=42
    )

    generator = SyntheticGenerator(
        model_id=os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct"),
        token=os.getenv("HF_TOKEN", ""),  # Optional Hugging Face token
        device=os.getenv("TEXT2ONTO_DEVICE", "auto"),
        extraction_method="openai",  # Optional: use "rule-based" instead
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_model="gpt-4o-mini",  # Used for generation-time extraction
    )

    train_synthetic = generator.generate(
        ontological_data=train_ontology, topic=ontology.domain
    )
    test_synthetic = generator.generate(
        ontological_data=test_ontology, topic=ontology.domain
    )
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

Preprocessing
^^^^^^^^^^^^^

``SyntheticDataPreprocessor.preprocess(synthetic_data, ontological_data)``
performs these five stages:

1. **Prepare records:** pair each document with the pseudo-sentences that
   generated it; derive ``is-a``, ``instance-of`` and applicable
   non-taxonomic triples.
2. **Clean text and labels:** insert missing spaces and remove unfinished
   trailing sentences where needed.
3. **Deep clean:** normalize text, entities, types and relation labels;
   remove invalid or duplicate triples; use LLM correction where configured.
4. **Check alignment:** an LLM judge assesses whether the text supports
   the triples. Aligned records and sufficiently rated partially aligned
   records are retained.
5. **Prepare task samples:** emit complete-triple samples for construction
   or initial-plus-extension samples for expansion.

Ontology Construction
^^^^^^^^^^^^^^^^^^^^^

Given a document, the learning target is its complete primitive ontology.
Select ``task="ontology_construction"`` and pass the generated data and
matching ontology partition to ``preprocess``. This example uses the
``train_synthetic``, ``test_synthetic`` and ``client`` defined above.

.. code-block:: python

    preprocessor = SyntheticDataPreprocessor(
        client=client,
        task="ontology_construction",  # Produce full ontology triples
    )
    train_data = preprocessor.preprocess(
        train_synthetic, train_ontology
    )
    test_data = preprocessor.preprocess(
        test_synthetic, test_ontology
    )

    print("training samples:", len(train_data))
    print("test samples:", len(test_data))

A construction sample has the following keys. The values below illustrate the
schema, not an extracted instance from a particular ontology.

.. code-block:: json

    {
      "id": "sample-001",
      "context": "Title: ...\n\n Content: \n...",
      "terms": ["example term"],
      "types": ["ExampleType"],
      "primitive-ontology-triples": [["ExampleType", "is-a", "ParentType"]]
    }

**Prediction target:** ``primitive-ontology-triples``. The learner must not
receive this gold target at inference time.

Ontology Expansion
^^^^^^^^^^^^^^^^^^

Given a document **and** initial primitive-ontology triples, the learning
target is the additional triples that extend that ontology. Use the shared
setup above; this is an alternative to the construction example.

.. code-block:: python

    preprocessor = SyntheticDataPreprocessor(
        client=client,
        task="ontology_expansion",  # Produce initial and extension triples
        random_state=42,  # Reproducible initial/extension split
    )
    train_data = preprocessor.preprocess(
        train_synthetic, train_ontology
    )
    test_data = preprocessor.preprocess(
        test_synthetic, test_ontology
    )

    print("training samples:", len(train_data))
    print("test samples:", len(test_data))

An expansion sample has the following structure (illustrative values):

.. code-block:: json

    {
      "id": "sample-002",
      "context": "Title: ...\n\n Content: \n...",
      "terms": ["example term"],
      "types": ["ExampleType"],
      "initial-primitive-ontology-triples": [["ParentType", "is-a", "Thing"]],
      "extended-primitive-ontology-triples": [["ExampleType", "is-a", "ParentType"]]
    }

The triples are shuffled and grouped by tail; the first half of each group,
with at least one triple overall, becomes the initial ontology. Remaining
triples are the extension target. Samples with no extension triples are
omitted. The ``terms`` and ``types`` fields refer to extension entities.

**Prediction input:** document plus ``initial-primitive-ontology-triples``.
**Prediction target:** ``extended-primitive-ontology-triples``.
