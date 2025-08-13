LLMs4OL Paradigm
====================================================

Learning Tasks
------------------------

OntoLearner's supports LLMs4OL three distinct paradigms for applying LLMs to ontology learning tasks, including:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Task**
     - **Description**
   * - **Term Typing**
     - Discover the generalized type for a lexical term.

       **ID**: ``term-typing``

       **Info**: The process of assigning a generalized type to each lexical term involves mapping lexical items to their most appropriate semantic categories or ontological classes. For example, in the biomedical domain, the term ``aspirin`` should be classified under ``Pharmaceutical Drug``. This task is crucial for organizing extracted terms into structured ontologies and improving knowledge reuse.

       **Example**: Assign the type ``"disease"`` to the term ``"myocardial infarction"``.
   * - **Taxonomy Discovery**
     - Discover the taxonomic hierarchy between type pairs.

       **ID**: ``taxonomy-discovery``

       **Info**: Taxonomy discovery focuses on identifying hierarchical relationships between types, enabling the construction of taxonomic structures (i.e., ``is-a`` relationships). Given a pair of terms or types, the task determines whether one is a subclass of the other. For example, discovering that ``Sedan is a subclass of Car`` contributes to structuring domain knowledge in a way that supports reasoning and inferencing in ontology-driven applications.

       **Example**: Recognize that ``"lung cancer"`` is a subclass of ``"cancer"``, which is a subclass of ``"disease"``.
   * - **Non-Taxonomic Relation Extraction**
     - Identify non-taxonomic, semantic relations between types.

       **ID**: ``non-taxonomic-re``

       **Info**: This task aims to extract non-hierarchical (non-taxonomic) semantic relations between concepts in an ontology. Unlike taxonomy discovery, which deals with is-a relationships, this task focuses on other meaningful associations such as part-whole (part-of), causal (causes), functional (used-for), and associative (related-to) relationships. For example, in a medical ontology, discovering that ``Aspirin treats Headache`` adds valuable relational knowledge that enhances the utility of an ontology.

       **Example**: Identify that *"virus"* ``causes`` *"infection"* or *"aspirin"* ``treats`` *"headache"*.

.. note::

    The ``ID`` field is essential for performing train-test splits and referencing specific instances during model training or evaluation.



For your own use-case, follow the best practices such as:

1. **Choose the Right Paradigm**: Selecting the appropriate learning paradigm is essential for effective ontology-related tasks. Pure LLM approaches work well for general or well-known domains where pre-trained models already have sufficient coverage. In contrast, RAG is better suited for specialized domains or when domain-specific training data is available. For high-stakes applications that demand higher reliability and robustness, ensemble methods combining LLMs with symbolic systems or multiple model outputs can offer the best performance.

2. **Optimize Prompting**: Prompt engineering plays a crucial role in guiding LLMs effectively. Clear and unambiguous instructions help reduce hallucinations and inconsistencies. When using RAG, it is important to provide relevant context alongside the prompt to ground the model's reasoning. Structured output formats (e.g., JSON, bullet points) make downstream processing easier. Experimenting with different prompt phrasings can further optimize task performance for your specific domain.

3. **Model Selection**: Choosing the right model involves balancing task complexity with available compute resources. Instruction-tuned models are a strong starting point, as they are trained to follow human-like instructions. Depending on the task, you should evaluate different models to identify which ones perform best in your domain. Larger models are often more capable of complex reasoning, but may not be feasible in constrained environments, so model size should be chosen accordingly.

4. **Evaluation Strategy**: A rigorous evaluation strategy ensures meaningful comparisons and prevents overfitting. Always use held-out test sets that are representative of your target distribution. Evaluation should go beyond a single metric — include standard (e.g., precision, recall, and F1) and domain-specific criteria (e.g., coverage, coherence of ontological axioms). It's also helpful to benchmark against classical ontology learning methods to measure the true added value of LLM-based approaches.

5. **Data Quality**: The effectiveness of RAG and fine-tuned models is heavily dependent on data quality. Training data should be clean, domain-relevant, and accurately labeled. Ontological relationships must be validated to avoid propagating structural errors. Inconsistencies in ground truth labels should be handled carefully to avoid misleading the model during training. For low-resource scenarios, thoughtful data augmentation can help expand coverage without compromising quality.

Tasks Datasets
-------------------------

The code below demonstrates how to load an ontology and use the .extract() method to retrieve datasets for LLMs4OL tasks.

.. code-block::

    from ontolearner import Wine

    ontology = Wine()

    ontology.load()

    data = ontology.extract()

    print(data)

The extracted ``data`` conforms to the ``OntologyData`` structure, which encapsulates the following data components:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Class**
     - **Description**
   * - ``OntologyData``
     - Main container for all ontological information.

       .. code-block:: python

           class OntologyData(BaseModel):
               term_typings: List[TermTyping]
               type_taxonomies: TypeTaxonomies
               type_non_taxonomic_relations: NonTaxonomicRelations
   * - ``TermTyping``
     - Represents term-to-type mappings.

       .. code-block:: python

           class TermTyping(BaseModel):
               ID: str         # Unique identifier
               term: str       # The term being typed
               types: List[str]  # List of types assigned to the term
   * - ``TaxonomicRelation``
     - Represents hierarchical (is-a) relationships between concepts.

       .. code-block:: python

           class TaxonomicRelation(BaseModel):
               ID: str       # Unique identifier
               parent: str   # Parent concept in hierarchy
               child: str    # Child concept in hierarchy
   * - ``NonTaxonomicRelation``
     - Represents non-hierarchical (semantic) relationships between concepts.

       .. code-block:: python

           class NonTaxonomicRelation(BaseModel):
               ID: str        # Unique identifier
               head: str      # Head entity in relation
               tail: str      # Tail entity in relation
               relation: str  # Type of relation


Train Test Splits
--------------------------

To perform machine learning tasks, the first step after extracting the dataset is to split it into training and testing sets. The following code demonstrates how to create these splits based on a specified ratio, with the resulting outputs formatted as ``OntologyData`` instances.

.. code-block:: python

    from ontolearner import Wine, train_test_split

    ontology = Wine()

    ontology.load()
    data = ontology.extract()

    train_data, test_data = train_test_split(data test_size=0.2, random_state=42)
