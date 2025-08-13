Ontology Hosting
==========================

Ontology Repositories
-----------------------

OntoLearner provides seamless integration with HuggingFace, allowing you to easily download ontologies and use. OntoLearner follows a systematic methodology for processing and distributing ontologies through Hugging Face. Each ontology undergoes a comprehensive processing pipeline that includes: (1) loading and parsing the original ontology file, (2) extracting structured learning datasets including term typings, taxonomic relations, and non-taxonomic relations, (3) computing detailed metrics about the ontology's topology and content, (4) generating comprehensive documentation, and (5) organizing the processed data by domain and uploading to dedicated Hugging Face repositories. This approach ensures that researchers have access to both the original ontologies and ready-to-use datasets optimized for machine learning applications, while maintaining full traceability and documentation of the processing methodology.


OntoLearner maintains a set of default repositories for each domain under the `SciKnowOrg <https://huggingface.co/collections/SciKnowOrg/>`_ organization. These repositories follow the naming pattern ``SciKnowOrg/ontolearner-{domain}`` and contain pre-processed ontology data.

.. hint::
   Each ontology repository on Hugging Face includes comprehensive documentation:

   * **README.md**: Contains information about the domain and available ontologies
   * **Usage Examples**: Code snippets showing how to use the ontologies

   See the `SciKnowOrg/ontolearner-agriculture <https://huggingface.co/datasets/SciKnowOrg/ontolearner-agriculture>`_ repository as an example.


The complete list of OntoLearner domain repositories is shown below:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - 🏷️ Domain
     - 🤗 HuggignFace Repository
     - 📝 Description
   * - `Agriculture <https://huggingface.co/datasets/SciKnowOrg/ontolearner-agriculture>`_
     - ``SciKnowOrg/ontolearner-agriculture``
     - Ontologies about farming systems, crops, food production, and agricultural vocabularies.
   * - `Arts and Humanities <https://huggingface.co/datasets/SciKnowOrg/ontolearner-arts_and_humanities>`_
     - ``SciKnowOrg/ontolearner-arts_and_humanities``
     - Ontologies that describe music, iconography, cultural artifacts, and humanistic content.
   * - `Biology and Life Sciences <https://huggingface.co/datasets/SciKnowOrg/ontolearner-biology_and_life_sciences>`_
     - ``SciKnowOrg/ontolearner-biology_and_life_sciences``
     - Ontologies about biological entities, systems, organisms, and molecular biology.
   * - `Chemistry <https://huggingface.co/datasets/SciKnowOrg/ontolearner-chemistry>`_
     - ``SciKnowOrg/ontolearner-chemistry``
     - Ontologies describing chemical entities, reactions, methods, and computational chemistry models.
   * - `Ecology and Environment <https://huggingface.co/datasets/SciKnowOrg/ontolearner-ecology_and_environment>`_
     - ``SciKnowOrg/ontolearner-ecology_and_environment``
     - Ontologies about ecological systems, environments, biomes, and sustainability science.
   * - `Education <https://huggingface.co/datasets/SciKnowOrg/ontolearner-education>`_
     - ``SciKnowOrg/ontolearner-education``
     - Ontologies describing learning content, educational programs, competencies, and teaching resources.
   * - `Events <https://huggingface.co/datasets/SciKnowOrg/ontolearner-events>`_
     - ``SciKnowOrg/ontolearner-events``
     - Ontologies for representing events, time, schedules, and calendar-based occurrences.
   * - `Finance <https://huggingface.co/datasets/SciKnowOrg/ontolearner-finance>`_
     - ``SciKnowOrg/ontolearner-finance``
     - Ontologies describing economic indicators, e-commerce, trade, and financial instruments.
   * - `Food and Beverage <https://huggingface.co/datasets/SciKnowOrg/ontolearner-food_and_beverage>`_
     - ``SciKnowOrg/ontolearner-food_and_beverage``
     - Ontologies related to food, beverages, ingredients, and culinary products.
   * - `General Knowledge <https://huggingface.co/datasets/SciKnowOrg/ontolearner-general_knowledge>`_
     - ``SciKnowOrg/ontolearner-general_knowledge``
     - Broad-scope ontologies and upper vocabularies used across disciplines for general-purpose semantic modeling.
   * - `Geography <https://huggingface.co/datasets/SciKnowOrg/ontolearner-geography>`_
     - ``SciKnowOrg/ontolearner-geography``
     - Ontologies for modeling spatial and geopolitical entities, locations, and place names.
   * - `Industry <https://huggingface.co/datasets/SciKnowOrg/ontolearner-industry>`_
     - ``SciKnowOrg/ontolearner-industry``
     - Ontologies describing industrial processes, smart buildings, manufacturing systems, and equipment.
   * - `Law <https://huggingface.co/datasets/SciKnowOrg/ontolearner-law>`_
     - ``SciKnowOrg/ontolearner-law``
     - Ontologies dealing with legal processes, regulations, and rights (e.g., copyright).
   * - `Library and Cultural Heritage <https://huggingface.co/datasets/SciKnowOrg/ontolearner-library_and_cultural_heritage>`_
     - ``SciKnowOrg/ontolearner-library_and_cultural_heritage``
     - Ontologies used in cataloging, archiving, and authority control of cultural and scholarly resources.
   * - `Materials Science and Engineering <https://huggingface.co/datasets/SciKnowOrg/ontolearner-materials_science_and_engineering>`_
     - ``SciKnowOrg/ontolearner-materials_science_and_engineering``
     - Ontologies related to materials, their structure, properties, processing, and engineering applications.
   * - `Medicine <https://huggingface.co/datasets/SciKnowOrg/ontolearner-medicine>`_
     - ``SciKnowOrg/ontolearner-medicine``
     - Ontologies covering clinical knowledge, diseases, drugs, treatments, and biomedical data.
   * - `News and Media <https://huggingface.co/datasets/SciKnowOrg/ontolearner-news_and_media>`_
     - ``SciKnowOrg/ontolearner-news_and_media``
     - Ontologies that model journalism, broadcasting, creative works, and media metadata.
   * - `Scholarly Knowledge <https://huggingface.co/datasets/SciKnowOrg/ontolearner-scholarly_knowledge>`_
     - ``SciKnowOrg/ontolearner-scholarly_knowledge``
     - Ontologies modeling the structure, process, and administration of scholarly research, publications, and infrastructure.
   * - `Social Sciences <https://huggingface.co/datasets/SciKnowOrg/ontolearner-social_sciences>`_
     - ``SciKnowOrg/ontolearner-social_sciences``
     - Ontologies for modeling societal structures, behavior, identity, and social interaction.
   * - `Units and Measurements <https://huggingface.co/datasets/SciKnowOrg/ontolearner-units_and_measurements>`_
     - ``SciKnowOrg/ontolearner-units_and_measurements``
     - Ontologies defining scientific units, quantities, dimensions, and observational models.
   * - `Upper Ontology <https://huggingface.co/datasets/SciKnowOrg/ontolearner-upper_ontology>`_
     - ``SciKnowOrg/ontolearner-upper_ontology``
     - Foundational ontologies that provide abstract concepts like objects, processes, and relations.
   * - `Web and Internet  <https://huggingface.co/datasets/SciKnowOrg/ontolearner-web_and_internet>`_
     - ``SciKnowOrg/ontolearner-web_and_internet``
     - Ontologies that model web semantics, linked data, APIs, and online communication standards.



Metrics Space
---------------

OntoLearner offers an interactive Metrics Space on HuggingFace that visualizes ontology metrics across many benchmarked domains. Available at the `SciKnowOrg/OntoLearner‑Benchmark‑Metrics <https://huggingface.co/spaces/SciKnowOrg/OntoLearner-Benchmark-Metrics>`_ space, it displays structured metrics for each ontology—such as total nodes, edges, classes, hierarchy depth, breadth, and dataset benchmarks like term types and relations  Researchers can explore ontology complexity and coverage visually, compare across domains, and validate suitability before using ontologies in learning tasks.


.. note::
       You can download the full ontology metrics Excel file from `this link <https://huggingface.co/spaces/SciKnowOrg/OntoLearner-Benchmark-Metrics/resolve/main/metrics.xlsx>`_.

.. hint::

   This file is automatically updated whenever a new ontology is modularized, ensuring you always have the latest benchmark metrics.
