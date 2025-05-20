HuggingFace Integration
==========================
OntoLearner provides integration with Hugging Face to easily load and share ontologies. This page explains how to use the Hugging Face integration features.

Downloading Ontologies from Hugging Face
---------------------------------------
OntoLearner allows you to download ontologies from any Hugging Face repository using the `download_from_huggingface` method:

.. code-block:: python

    from ontolearner.ontology import Wine

    # Download from repository
    ontology = Wine()
    file_path = ontology.download_from_huggingface()

Loading Ontologies from Hugging Face
------------------------------------
After downloading an ontology, you can load it using the `load` method:

.. code-block:: python

    from ontolearner.ontology import Wine

    # Download and load
    ontology = Wine()
    file_path = ontology.download_from_huggingface()
    ontology.load(file_path)

    # Now you can extract data
    data = ontology.extract()

Default Hugging Face Repositories
--------------------------------
OntoLearner maintains a set of default repositories for each domain under the `SciKnowOrg` organization.
These repositories follow the naming pattern `SciKnowOrg/ontolearner-{domain}` and contain pre-processed ontology data.
When you don't specify a custom repository, OntoLearner will automatically use these default repositories based on the ontology's domain.

Complete Example
---------------
Here's a complete example of downloading, loading, and using an ontology from Hugging Face:

.. code-block:: python

    from ontolearner.ontology import Wine
    from ontolearner.utils.train_test_split import ontology_train_test_split

    # Download and load the ontology
    ontology = Wine()
    file_path = ontology.download_from_huggingface()
    ontology.load(file_path)

    # Extract data
    data = ontology.extract()

    # Use the data for training and evaluation
    train_data, test_data = ontology_train_test_split(data, test_size=0.2)

    # Now you can use the data with your learner models
