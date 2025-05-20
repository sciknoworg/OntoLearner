HuggingFace
==========================
OntoLearner maintains a set of default repositories for each domain under the `SciKnowOrg` organization.
These repositories follow the naming pattern `SciKnowOrg/ontolearner-{domain}` and contain pre-processed ontology data.

Basic Usage
-----------
The simplest way to load an ontology from Hugging Face:

.. code-block:: python

    from ontolearner.ontology import Wine
    ontology = Wine()
    ontology.load()  # automatically downloads from HuggingFace
    data = ontology.extract()
