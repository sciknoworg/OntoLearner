Quickstart
================

Ontologizer
--------------------

In OntoLearner, Ontologizers provide a programmatic interface for working with ontologies directly in Python. They offer a standardized way to load, process, and extract structured knowledge from ontological sources for a variety of applications, including ontology learning tasks and other Semantic Web use cases. OntoLearner includes built-in access to several standard ontologies. Below is an example using the `Agronomy Ontology <https://ontolearner.readthedocs.io/benchmarking/agriculture/agro.html#agronomy-ontology-agro>`_  (``ArgO``), which is automatically retrieved from our `🤗 HuggingFace repository <https://huggingface.co/collections/SciKnowOrg/>`_ upon loading.

.. sidebar:: 📰 See Also

    - `Documentation for existing ontologies <https://ontolearner.readthedocs.io/benchmarking/benchmark.html>`_
    - `How to work with Ontologizers <https://ontolearner.readthedocs.io/ontologizer/ontologizer.html>`_

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


Learner Models
------------------

OntoLearner supports three fundamental ontology learning tasks that enable automated knowledge extraction and ontology construction from existing ontological data. The tasks are defined as follows:

- Term Typing: Discover the generalized type for a lexical term
Once domain-relevant terms and types are extracted (as we explored in Task A - Text2Onto), the next step is to assign a generalized type to each lexical term. This process involves mapping lexical items to their most appropriate semantic categories or ontological classes. For example, in the biomedical domain, the term “aspirin” should be classified under “Pharmaceutical Drug”. This task is crucial for organizing extracted terms into structured ontologies and improving knowledge reuse.


These tasks form the core of the library’s machine learning capabilities and are designed to work with various learner models including retrieval-based, LLM-based, and Retrieval-Augmented Generation (RAG) approaches.
To alighn with machine learning follow, once the ontology is loaded, we can extract the learning examples and split them into training and testing subsets for further learning procedures.

Benchmarking
----------------


3. Extract and Split the Data
-----------------------------


.. code-block:: python

   from ontolearner import train_test_split

   train_data, test_data = train_test_split(
       ontology.extract(),
       test_size=0.2,
       random_state=42
   )

Explanation:

- `.extract()` retrieves candidate triples or axioms for a selected learning task.
- `train_test_split()` is a utility function for random shuffling and splitting (80/20 here).

4. Configure the Learning Pipeline
----------------------------------

We now configure the learner pipeline using a small instruction-tuned model (`Qwen`) and a retriever model:

.. code-block:: python

   from ontolearner import LearnerPipeline

   pipeline = LearnerPipeline(
       retriever_id='sentence-transformers/all-MiniLM-L6-v2',
       llm_id='Qwen/Qwen2.5-0.5B-Instruct',
       hf_token='<YOUR_HF_TOKEN>',
       batch_size=16,
       top_k=3
   )

Explanation:

- `retriever_id`: Semantic retriever that retrieves relevant context from ontology fragments.
- `llm_id`: The instruction-following language model used to generate candidate outputs.
- `top_k`: Number of retrieved examples passed to the LLM (used in RAG setup).
- `hf_token`: Required for loading gated models from Hugging Face.

5. Run the Pipeline
-------------------

Once configured, the pipeline is executed on the training and test data:

.. code-block:: python

   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       evaluate=True,
       task='non-taxonomic-re'
   )

Explanation:

- `task`: One of `term-typing`, `taxonomy-discovery`, or `non-taxonomic-re`.
- `evaluate=True`: Computes performance metrics like precision, recall, and F1-score.
- Returns a dictionary with predictions, metrics, logs, and timing.

6. Evaluate the Results
------------------------

You can inspect the metrics and runtime performance:

.. code-block:: python

   print("Metrics:", outputs['metrics'])
   print("Elapsed time:", outputs['elapsed_time'])

Explanation:

- Useful to monitor model accuracy and speed.
- Helps compare different LLM/retriever configurations across tasks.

7. Explore Predictions
-----------------------

You can examine a few sample predictions for inspection:

.. code-block:: python

   import pandas as pd

   pd.DataFrame(outputs['predictions'][:5])

Explanation:

- Displays the first 5 predictions in a readable format.
- Each row may include the input, predicted output, true label (if available), and confidence scores.

8. Run in Google Colab
-----------------------

To interactively run this tutorial, use the Colab notebook provided here:

`Open in Colab <https://colab.research.google.com/drive/1DuElAyEFzd1vtqTjDEXWcc0zCbiV2Yee?usp=sharing>`_

.. note::

   Ensure your Hugging Face token has access to gated models like `Qwen2.5-0.5B-Instruct`. You can get one at https://huggingface.co/settings/tokens.

---

This quickstart guide should help you get started with `OntoLearner` in minutes. For more complex tasks or datasets, refer to the full documentation and examples.
