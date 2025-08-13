Quickstart
================

Ontologizer
--------------------


In OntoLearner, Ontologizers provide a programmatic interface for working with ontologies directly in Python. They offer a standardized way to load, process, and extract structured knowledge from ontological sources for a variety of applications, including ontology learning tasks and other Semantic Web use cases.
OntoLearner includes built-in access to several standard ontologies.


Below is an example using the `Agronomy Ontology <https://ontolearner.readthedocs.io/benchmarking/agriculture/agro.html#agronomy-ontology-agro>`_  (``ArgO``), which is automatically retrieved from our `🤗 HuggingFace repository <https://huggingface.co/collections/SciKnowOrg/>`_ upon loading.

.. hint::
     **Available domains**: Biology, Chemistry, Medicine, Agriculture, Environment, Geography, Industry, Materials Science, Law, Finance • and more!

.. sidebar:: 📰 See Also

    - `Explore 150+ Ready-to-Use Ontologies <https://ontolearner.readthedocs.io/benchmarking/benchmark.html>`_
    - `How to work with Ontologizers <https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html>`_


.. code-block:: python

   from ontolearner import AgrO

   ontology = AgrO() # Initialize the ontology

   ontology.load() # Load the ontology (from HuggingFace by default)
   # To load from a local file, pass the path as an argument:
   # ontology.load(path="path/to/file.owl")

   print(ontology) # Print metadata
   # Sample output:
   # ontology_id: AgrO
   # ontology_full_name: Agronomy Ontology (AgrO)
   # domain: Agriculture
   # category: Agronomy
   # version: 1.0
   # last_updated: 2022-11-02
   # creator: The Crop Ontology Consortium
   # license: Creative Commons 4.0
   # format: RDF
   # download_url: https://agroportal.lirmm.fr/ontologies/AGRO?p=summary

.. note::

    - ``AgrO()``  is a built-in Ontologizer class in OntoLearner.
    - ``.load()`` fetches and parses the ontology into a structured internal format.




Ontology Learning Tasks
------------------------

Ontology Learning plays a crucial role in dynamically building and maintaining ontologies, which are essential for intelligent applications in knowledge graphs, information retrieval, question answering, and more. OntoLearner uses a LLMs4OL paradigm tasks to provide the capability to use LLMs for ontology learning tasks. The goal is to transition from raw text or structured corpora to formal knowledge representations such as classes, properties, and axioms.

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/images/LLMs4OL.png" alt="OntoLearner Logo" width="100%"/>
   </div>


As a presented in the above figure, core ontology learning tasks within OntoLearner are:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Task
     - Description
   * - **Term Typing**
     - Associate each lexical entry with its appropriate conceptual type or class.

       **Example**: Assign the type ``"disease"`` to the term ``"myocardial infarction"``.
   * - **Taxonomy Discovery**
     - Construct a taxonomic hierarchy by identifying subclass-superclass relationships between types.

       **Example**: Recognize that ``"lung cancer"`` is a subclass of ``"cancer"``, which is a subclass of ``"disease"``.
   * - **Non-Taxonomic Relation Extraction**
     - Discover non-hierarchical semantic relations between types or terms.

       **Example**: Identify that *"virus"* ``causes`` *"infection"* or *"aspirin"* ``treats`` *headache*.

Additionally, we introduced a new task to address the **terminology extraction** phase.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Task
     - Description
   * - **Text2Onto**
     - Extract ontological terminologies and conceptual types from raw text.

       **Example**: Extract terms like ``"heart attack"`` and assign preliminary types such as ``"medical event"`` or ``"disease"``.

These tasks can be performed sequentially or in parallel, depending on the learning strategy. The outputs of earlier stages (e.g., term extraction and typing) often serve as inputs for later stages (e.g., hierarchy induction).

OntoLearner supports automatic dataset extraction for the ontology learning tasks described above. Once an ontology is loaded, simply calling the ``.extract()`` method will generate the corresponding datasets.

.. code-block:: python

   from ontolearner import AgrO

   ontology = AgrO()

   ontology.load()

   ontological_data = ontology.extract()

The ``.extract()`` retrieves candidate triples or axioms for a selected learning task. The extracted data follows ``OntologyData`` schema. This is the main data container that aggregates all three types of ontological information needed for machine learning tasks. It represents the complete structured knowledge extracted from an ontology file.

.. hint:: ``OntologyData`` Schema:

    - `term_typings`: All term-to-type mappings for learning type prediction.
    - `type_taxonomies`: All hierarchical relationships and involved types.
    - `type_non_taxonomic_relations`: All semantic associations and relation types.


Learner Models
------------------

To alighn with machine learning follow, once the ontology is loaded, and ontological data extracted, we can split them into training and testing subsets for further learning procedures.

.. code-block:: python

   from ontolearner import train_test_split

   # A utility function for random shuffling and splitting (80/20 here).
   train_data, test_data = train_test_split(
       ontology.extract(),
       test_size=0.2,
       random_state=42
   )


Once the data is split into training and testing sets, you can apply learning models to the ontology learning tasks. OntoLearner supports multiple modeling approaches, including retrieval-based methods, Large Language Model (LLM)-based techniques, and Retrieval-Augmented Generation (RAG) strategies. The ``LearnerPipeline`` within OntoLearner is designed for ease of use, abstracting away the complexities of loading models and preparing datasets or data loaders. You can configure the pipeline with your choice of LLMs, retrievers, or RAG components.

In the example below, we configure a RAG-based learner by specifying the Qwen LLM (`Qwen/Qwen2.5-0.5B-Instruct <https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct>`_) and a retriever based on a sentence-transformer model (`all-MiniLM-L6-v2 <https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2>`_):

.. sidebar:: Other Learners

    To experiment with an LLM-based learner, simply provide the ``llm_id`` and leave the ``retriever_id`` unset.
    Likewise, for a retriever-only learner, specify the ``retriever_id`` and omit the ``llm_id``.


.. code-block:: python

   from ontolearner import LearnerPipeline

   pipeline = LearnerPipeline(
       retriever_id='sentence-transformers/all-MiniLM-L6-v2',
       llm_id='Qwen/Qwen2.5-0.5B-Instruct',
       hf_token='<YOUR_HF_TOKEN>',
       batch_size=16,
       top_k=3
   )

.. note::

    - ``retriever_id``: Semantic retriever that retrieves relevant context from ontology fragments.
    - ``llm_id``: The instruction-following language model used to generate candidate outputs.
    - ``top_k``: Number of retrieved examples passed to the LLM (used in RAG setup).
    - ``hf_token``: Required for loading gated models from Hugging Face.

Once configured, the pipeline is executed on the training and test data:

.. code-block:: python

   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       evaluate=True,
       task='non-taxonomic-re'
   )

   print("Metrics:", outputs['metrics'])
   print("Elapsed time:", outputs['elapsed_time'])
   print(outputs['predictions'][:5])


Once the execution is done, it returns a dictionary with predictions, evaluation metrics, and timing. Here ``task`` variable can be one of `term-typing`, `taxonomy-discovery`, or `non-taxonomic-re`. The ``evaluate=True``, results in computation of performance metrics like precision, recall, and F1-score.

.. warning::

   Ensure your Hugging Face token has access to gated models. You can get one at https://huggingface.co/settings/tokens.


What's Next?
---------------

* :doc:`ontologizer/ontology_modularization` - How Ontologizer works.
* :doc:`ontologizer/ontology_hosting` - Checkout avaiable domains and their repositories.
* :doc:`learning_tasks/learning_tasks` - Deep dive into all three tasks
* :doc:`learning_tasks/text2onto` - How Text2Onto works?
