Ontology Modularization
==============================

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/main/docs/source/images/Ontologizer.jpg" alt="OntoLearner Logo" width="90%"/>
   </div>
   <br>


**Ontologizer** is a foundational module within OntoLearner that transforms ontologies into programmatically accessible Python objects, enabling seamless loading, inspection, and reuse across diverse domains. It supports multiple ontology formats (OWL, RDF, XML, TTL) and integrates metadata management, automated metric evaluation, and documentation generation to ensure ontologies are FAIR-compliant and traceable. By allowing users to import ontologies directly from web sources or `HuggingFace repositories <https://huggingface.co/collections/SciKnowOrg/>`_ without manual file handling, Ontologizer simplifies ontology modularization and promotes scalable, cross-domain ontology enrichment. Its design supports version control and collaborative updates, while optimizing performance for large ontologies through multiprocessing, ultimately providing a flexible, user-friendly foundation for ontology-driven workflows and research.


Programmatic Import
-----------------------------------
OntoLearner provides a convenient interface to load and interact with popular ontologies directly from Hugging Face, making it easy to kickstart ontology-based learning tasks.

.. code-block:: python

    from ontolearner import Wine

    ontology = Wine()

    ontology.load()  # Automatically downloads and prepares ontology

    data = ontology.extract()  # Returns learning tasks data

This will automatically download the ontology file and pre-processed datasets from the appropriate Hugging Face repository.

.. sidebar:: Load

    The ``.load`` method handles loading ontology from local and HuggingFace cases. If a ``path`` is provided as an argument, it will load the ontology from the local file system. Otherwise, it will attempt to retrieve the ontology from Hugging Face.


.. tab:: Load Ontology from Local

   Use this method when the ontology file is stored on your local system:

   .. code-block:: python

        ontology.from_local(path="path/to/ontology/file")

.. tab:: Load Ontology from HuggingFace

   This method allows loading the ontology directly from the Hugging Face repository. No additional input (e.g., path) is required, as it uses the metadata defined in the Ontologizer to locate and retrieve the ontology automatically:

   .. code-block:: python

        ontology.from_huggingface()



You can also access and work with domain-specific ontologies using intuitive import patterns, here are more examples:

.. code-block:: python

    from ontolearner import ENVO, ChEBI, MGED, AFO

    # 🌱 Environmental science ontology
    ontology = ENVO()

    # ⚗️ Chemistry ontology (Chemical Entities of Biological Interest)
    ontology = ChEBI()

    # 🧬 Gene expression and microarray ontology
    ontology = MGED()

    # 🚜 Agriculture ontology (Agricultural Field Ontology)
    ontology = AFO()

Each of these ontologies is tied to a specific domain repository on Hugging Face and includes both raw files and structured datasets, ready for training, evaluation, or integration into downstream pipelines.




Inspecting Metadata
---------------------------------

Once an ontology is loaded, you can inspect its metadata by simply printing the ontology object. This outputs essential information encoded during modularization—capturing attributes that ensure traceability, version control, and alignment with FAIR principles. These metadata fields not only describe the ontology’s origin and scope but also support filtering, documentation, and automated validation during training or inference workflows.

.. code-block:: python

    from ontolearner import AgrO

    ontology = AgrO()

Which will results in:

.. code-block:: cmd

    ontology_id: AgrO
    ontology_full_name: Agronomy Ontology (AgrO)
    domain: Agriculture
    category: Agronomy
    version: 1.0
    last_updated: 2022-11-02
    creator: The Crop Ontology Consortium
    license: Creative Commons 4.0
    format: RDF
    download_url: https://agroportal.lirmm.fr/ontologies/AGRO?p=summary

This metadata snapshot allows users to quickly verify the ontology's provenance, licensing, and format before usage. It also aids in reproducibility and collaboration by making ontology versioning and source links transparent within the OntoLearner ecosystem.

Automatic Usage
-----------------------------------
For flexible and dynamic loading of ontologies without hardcoding class names, use the ``AutoOntology`` interface. This is particularly useful when handling multiple ontologies programmatically or when ontology IDs are provided at runtime.

.. code-block:: python

    from ontolearner import AutoOntology

    ontology = AutoOntology("AgrO")

This command automatically resolves and loads the specified ontology (in this case, the ``AgrO``) by referencing its ``ontology_id``. Behind the scenes, AutoOntology maps the identifier to its corresponding modularized class and metadata, streamlining workflows that require scalable, ontology-agnostic operations.

.. hint::
   Each ontology listed on the `Benchmarked Ontologies <https://ontolearner.readthedocs.io/benchmarking/benchmark.html>`_ is accompanied by detailed documentation such as:

   * Short description on the ontology
   * Metadata table followed by ontology metrics.
   * Code snippets showing how to import the ontologies

   For example, see the `Chemical Entities of Biological Interest (ChEBI) ontology  <https://ontolearner.readthedocs.io/benchmarking/chemistry/chebi.html>`_ page.
