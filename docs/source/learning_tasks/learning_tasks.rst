Learning Tasks
================
OntoLearner supports three fundamental ontology learning tasks
that enable automated knowledge extraction and ontology construction
from existing ontological data. These tasks form the core of the library's
machine learning capabilities and are designed to work with various learner models
including retrieval-based, LLM-based, and hybrid RAG (Retrieval-Augmented Generation) approaches.

Overview
--------
The learning tasks in OntoLearner follow a standard machine learning workflow:

1. **Data Loading**: Extract structured data from existing ontologies
2. **Train-Test Split**: Divide data to prevent overfitting and enable evaluation
3. **Model Training**: Train learners using various approaches (retrieval, LLM, RAG)
4. **Prediction**: Apply trained models to new data
5. **Evaluation**: Assess performance using task-specific metrics

All tasks operate on the ``OntologyData`` structure, which contains three main components:

- ``term_typings``: List of term-to-type mappings
- ``type_taxonomies``: Hierarchical relationships between types
- ``type_non_taxonomic_relations``: Non-hierarchical relationships between types

Supported Tasks
---------------

Task 1: Term Typing
~~~~~~~~~~~~~~~~~~~
**Objective**: Predict the semantic type(s) of a given term.

**Description**: Term typing involves determining what category or class a specific term belongs to within an ontological framework. For example, predicting that "ChardonnayGrape" is a "WineGrape" in the context of a wine ontology.

**Example Usage**:

.. code-block:: python

    from ontolearner import LearnerPipeline, Wine, train_test_split

    # Load ontology and extract data
    ontology = Wine()
    ontology.load()
    data = ontology.extract()

    # Split data
    train_data, test_data = train_test_split(data, test_size=0.2)

    # Create pipeline for term typing
    pipeline = LearnerPipeline(
        task="term-typing",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1",
        hf_token="your_huggingface_token"
    )

    # Train and evaluate
    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        top_k=3,
        test_limit=10
    )

    print(f"Average F1-Score: {metrics['avg_f1_score']:.3f}")
    print(f"Average Exact Match: {metrics['avg_exact_match']:.3f}")


Task 2: Taxonomy Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~
**Objective**: Identify hierarchical "is-a" relationships between types.

**Description**: Taxonomy discovery involves determining whether one concept is a subclass or specialization of another. This task builds the hierarchical backbone of ontologies by identifying parent-child relationships.

**Example Usage**:

.. code-block:: python

    from ontolearner import LearnerPipeline, AutoLearnerLLM, Wine, train_test_split

    # Load and prepare data
    ontology = Wine()
    ontology.load()
    train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

    # Create pipeline for taxonomy discovery
    pipeline = LearnerPipeline(
        task="taxonomy-discovery",
        llm=AutoLearnerLLM(token="your_huggingface_token"),
        llm_id="mistralai/Mistral-7B-Instruct-v0.1"
    )

    # Train and evaluate
    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        test_limit=10
    )

    print(f"Average Accuracy: {metrics['avg_accuracy']:.3f}")

Task 3: Non-Taxonomic Relation Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Objective**: Identify non-hierarchical relationships between concepts.

**Description**: Non-taxonomic relation discovery involves predicting semantic relationships that are not "is-a" relationships. These include relationships like "hasColor", "locatedIn", "producedBy", etc.

**Example Usage**:

.. code-block:: python

    from ontolearner import LearnerPipeline, BERTRetrieverLearner, Wine, train_test_split

    # Load and prepare data
    ontology = Wine()
    ontology.load()
    train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

    # Create pipeline for non-taxonomic relation discovery
    pipeline = LearnerPipeline(
        task="non-taxonomy-discovery",
        retriever=BERTRetrieverLearner(),
        retriever_id="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Train and evaluate
    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        top_k=5,
        test_limit=10
    )

    print(f"Average Exact Match: {metrics['avg_exact_match']:.3f}")
    print(f"Average Similarity: {metrics['avg_similarity']:.3f}")


Data Structures
---------------
**OntologyData**: Main container for all ontological information

.. code-block:: python

    class OntologyData(BaseModel):
        term_typings: List[TermTyping]
        type_taxonomies: TypeTaxonomies
        type_non_taxonomic_relations: NonTaxonomicRelations

**TermTyping**: Represents term-to-type mappings

.. code-block:: python

    class TermTyping(BaseModel):
        ID: str  # Unique identifier
        term: str  # The term being typed
        types: List[str]  # List of types assigned to the term

**TaxonomicRelation**: Represents hierarchical relationships

.. code-block:: python

    class TaxonomicRelation(BaseModel):
        ID: str  # Unique identifier
        parent: str  # Parent concept in hierarchy
        child: str  # Child concept in hierarchy

**NonTaxonomicRelation**: Represents non-hierarchical relationships

.. code-block:: python

    class NonTaxonomicRelation(BaseModel):
        ID: str  # Unique identifier
        head: str  # Head entity in relation
        tail: str  # Tail entity in relation
        relation: str  # Type of relation
