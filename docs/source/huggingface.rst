HuggingFace Integration
==========================
OntoLearner provides seamless integration with Hugging Face,
allowing you to easily download ontologies and use pre-trained models.

Ontology Repositories
--------------------
OntoLearner maintains a set of default repositories for each domain under the `SciKnowOrg` organization.
These repositories follow the naming pattern `SciKnowOrg/ontolearner-{domain}` and contain pre-processed ontology data.

Available domains include:
- `SciKnowOrg/ontolearner-agriculture <https://huggingface.co/datasets/SciKnowOrg/ontolearner-agriculture>`_
- `SciKnowOrg/ontolearner-biology <https://huggingface.co/datasets/SciKnowOrg/ontolearner-biology>`_
- `SciKnowOrg/ontolearner-chemistry <https://huggingface.co/datasets/SciKnowOrg/ontolearner-chemistry>`_
- `SciKnowOrg/ontolearner-general_knowledge <https://huggingface.co/datasets/SciKnowOrg/ontolearner-general_knowledge>`_
- `SciKnowOrg/ontolearner-materials_science_and_engineering <https://huggingface.co/datasets/SciKnowOrg/ontolearner-materials_science_and_engineering>`_
- And more...

Loading Ontologies from Hugging Face
-----------------------------------
The simplest way to load an ontology from Hugging Face:

.. code-block:: python

    from ontolearner.ontology import Wine
    ontology = Wine()
    ontology.load()  # automatically downloads from HuggingFace
    data = ontology.extract()

This will automatically download the ontology file and pre-processed datasets from the appropriate Hugging Face repository.

Using Pre-trained Models from Hugging Face
-----------------------------------------
OntoLearner also supports using pre-trained models from Hugging Face for both retrieval and LLM components:

.. code-block:: python

    from ontolearner.learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner
    from ontolearner.learner.prompt import StandardizedPrompting

    retriever = BERTRetrieverLearner()
    llm = AutoLearnerLLM(token="your_huggingface_token")
    prompting = StandardizedPrompting(task="term-typing")

    rag_learner = AutoRAGLearner(retriever, llm, prompting)

    rag_learner.load(
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1"
    )

Authentication
-------------
Some models on Hugging Face require authentication. You can provide your Hugging Face token in several ways:
1. **Environment Variable**: Set the `HUGGINGFACE_ACCESS_TOKEN` environment variable
2. **Direct Parameter**: Pass the token directly to the constructor:

   .. code-block:: python

       llm = AutoLearnerLLM(token="your_huggingface_token")

3. **.env File**: Create a `.env` file with your token:

   .. code-block:: text

       HUGGINGFACE_ACCESS_TOKEN=your_huggingface_token

   Then load it in your script:

   .. code-block:: python

       from dotenv import find_dotenv, load_dotenv
       _ = load_dotenv(find_dotenv())

Citation and Documentation
-------------------------
Each ontology repository on Hugging Face includes:

1. **README.md**: Contains information about the domain and available ontologies
2. **Citation Information**: How to cite the ontologies in academic work
3. **Usage Examples**: Code snippets showing how to use the ontologies

For example, see the `SciKnowOrg/ontolearner-agriculture <https://huggingface.co/datasets/SciKnowOrg/ontolearner-agriculture>`_ repository.
