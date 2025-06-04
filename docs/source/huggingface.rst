HuggingFace Integration
==========================
OntoLearner provides seamless integration with Hugging Face,
allowing you to easily download ontologies and use pre-trained models.

Methodology
-----------

OntoLearner follows a systematic methodology for processing and distributing ontologies through Hugging Face. Each ontology undergoes a comprehensive processing pipeline that includes: (1) loading and parsing the original ontology file, (2) extracting structured learning datasets including term typings, taxonomic relations, and non-taxonomic relations, (3) computing detailed metrics about the ontology's topology and content, (4) generating comprehensive documentation, and (5) organizing the processed data by domain and uploading to dedicated Hugging Face repositories. This approach ensures that researchers have access to both the original ontologies and ready-to-use datasets optimized for machine learning applications, while maintaining full traceability and documentation of the processing methodology.

Ontology Repositories
--------------------
OntoLearner maintains a set of default repositories for each domain under the `SciKnowOrg` organization.
These repositories follow the naming pattern `SciKnowOrg/ontolearner-{domain}` and contain pre-processed ontology data.

Available domains include:

.. list-table:: OntoLearner Domain Repositories
   :header-rows: 1
   :widths: 25 15 60

   * - Domain
     - Repository
     - Description
   * - Agriculture
     - `ontolearner-agriculture <https://huggingface.co/datasets/SciKnowOrg/ontolearner-agriculture>`_
     - Ontologies about farming systems, crops, food production, and agricultural vocabularies.
   * - Arts and Humanities
     - `ontolearner-arts_and_humanities <https://huggingface.co/datasets/SciKnowOrg/ontolearner-arts_and_humanities>`_
     - Ontologies that describe music, iconography, cultural artifacts, and humanistic content.
   * - Biology and Life Sciences
     - `ontolearner-biology_and_life_sciences <https://huggingface.co/datasets/SciKnowOrg/ontolearner-biology_and_life_sciences>`_
     - Ontologies about biological entities, systems, organisms, and molecular biology.
   * - Chemistry
     - `ontolearner-chemistry <https://huggingface.co/datasets/SciKnowOrg/ontolearner-chemistry>`_
     - Ontologies describing chemical entities, reactions, methods, and computational chemistry models.
   * - Ecology and Environment
     - `ontolearner-ecology_and_environment <https://huggingface.co/datasets/SciKnowOrg/ontolearner-ecology_and_environment>`_
     - Ontologies about ecological systems, environments, biomes, and sustainability science.
   * - Education
     - `ontolearner-education <https://huggingface.co/datasets/SciKnowOrg/ontolearner-education>`_
     - Ontologies describing learning content, educational programs, competencies, and teaching resources.
   * - Events
     - `ontolearner-events <https://huggingface.co/datasets/SciKnowOrg/ontolearner-events>`_
     - Ontologies for representing events, time, schedules, and calendar-based occurrences.
   * - Finance
     - `ontolearner-finance <https://huggingface.co/datasets/SciKnowOrg/ontolearner-finance>`_
     - Ontologies describing economic indicators, e-commerce, trade, and financial instruments.
   * - Food and Beverage
     - `ontolearner-food_and_beverage <https://huggingface.co/datasets/SciKnowOrg/ontolearner-food_and_beverage>`_
     - Ontologies related to food, beverages, ingredients, and culinary products.
   * - General Knowledge
     - `ontolearner-general_knowledge <https://huggingface.co/datasets/SciKnowOrg/ontolearner-general_knowledge>`_
     - Broad-scope ontologies and upper vocabularies used across disciplines for general-purpose semantic modeling.
   * - Geography
     - `ontolearner-geography <https://huggingface.co/datasets/SciKnowOrg/ontolearner-geography>`_
     - Ontologies for modeling spatial and geopolitical entities, locations, and place names.
   * - Industry
     - `ontolearner-industry <https://huggingface.co/datasets/SciKnowOrg/ontolearner-industry>`_
     - Ontologies describing industrial processes, smart buildings, manufacturing systems, and equipment.
   * - Law
     - `ontolearner-law <https://huggingface.co/datasets/SciKnowOrg/ontolearner-law>`_
     - Ontologies dealing with legal processes, regulations, and rights (e.g., copyright).
   * - Library and Cultural Heritage
     - `ontolearner-library_and_cultural_heritage <https://huggingface.co/datasets/SciKnowOrg/ontolearner-library_and_cultural_heritage>`_
     - Ontologies used in cataloging, archiving, and authority control of cultural and scholarly resources.
   * - Materials Science and Engineering
     - `ontolearner-materials_science_and_engineering <https://huggingface.co/datasets/SciKnowOrg/ontolearner-materials_science_and_engineering>`_
     - Ontologies related to materials, their structure, properties, processing, and engineering applications.
   * - Medicine
     - `ontolearner-medicine <https://huggingface.co/datasets/SciKnowOrg/ontolearner-medicine>`_
     - Ontologies covering clinical knowledge, diseases, drugs, treatments, and biomedical data.
   * - News and Media
     - `ontolearner-news_and_media <https://huggingface.co/datasets/SciKnowOrg/ontolearner-news_and_media>`_
     - Ontologies that model journalism, broadcasting, creative works, and media metadata.
   * - Scholarly Knowledge
     - `ontolearner-scholarly_knowledge <https://huggingface.co/datasets/SciKnowOrg/ontolearner-scholarly_knowledge>`_
     - Ontologies modeling the structure, process, and administration of scholarly research, publications, and infrastructure.
   * - Social Sciences
     - `ontolearner-social_sciences <https://huggingface.co/datasets/SciKnowOrg/ontolearner-social_sciences>`_
     - Ontologies for modeling societal structures, behavior, identity, and social interaction.
   * - Units and Measurements
     - `ontolearner-units_and_measurements <https://huggingface.co/datasets/SciKnowOrg/ontolearner-units_and_measurements>`_
     - Ontologies defining scientific units, quantities, dimensions, and observational models.
   * - Upper Ontology
     - `ontolearner-upper_ontology <https://huggingface.co/datasets/SciKnowOrg/ontolearner-upper_ontology>`_
     - Foundational ontologies that provide abstract concepts like objects, processes, and relations.
   * - Web and Internet
     - `ontolearner-web_and_internet <https://huggingface.co/datasets/SciKnowOrg/ontolearner-web_and_internet>`_
     - Ontologies that model web semantics, linked data, APIs, and online communication standards.

Loading Ontologies from Hugging Face
-----------------------------------
The simplest way to load an ontology from Hugging Face:

.. code-block:: python

    from ontolearner.ontology import Wine
    ontology = Wine()
    ontology.load()  # automatically downloads from HuggingFace
    data = ontology.extract()

This will automatically download the ontology file and pre-processed datasets from the appropriate Hugging Face repository.

.. hint::
   Each ontology repository on Hugging Face includes comprehensive documentation:

   * **README.md**: Contains information about the domain and available ontologies
   * **Citation Information**: How to cite the ontologies in academic work
   * **Usage Examples**: Code snippets showing how to use the ontologies

   For example, see the `SciKnowOrg/ontolearner-agriculture <https://huggingface.co/datasets/SciKnowOrg/ontolearner-agriculture>`_ repository.
