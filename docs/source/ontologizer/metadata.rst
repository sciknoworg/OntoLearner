Metadata
=============================

.. note::

	OntoLearner Metadata will be created automatically at Github under `metadata/ <https://github.com/sciknoworg/OntoLearner/tree/main/metadata>`_ directory, and it is available for download after ``ontolearner > 1.4.0`` also at `Releases <https://github.com/sciknoworg/OntoLearner/releases>`_ per release.

.. hint::

	The metadata release is fully automated through CI/CD, ensuring it is generated automatically with each PyPI release.

.. sidebar:: OntoLearner Metadata Exporter Features

	- Generates `Dublin Core metadata <https://www.dublincore.org/specifications/dublin-core/dces/>`_ for each ontology in the library
	- Creates a top-level ``Collection`` resource for OntoLearner
	- Supports RDF/XML serialization in a clean, human-readable format
	- Uses a custom ``ontologizer`` namespace for ontology-specific resources


The ``OntoLearnerMetadataExporter`` is a utility class for generating **Dublin Core (DCMI) metadata** for all ontologies benchmarked in the OntoLearner library. It collects essential metadata, including ontology title and description, creator/authors, license information, format, version, and last updated date, domain and category, and download URL. Additionally, it generates a **top-level collection resource** that describes the entire OntoLearner benchmarking suite. The output is a **pretty-printed RDF/XML file** compatible with standard semantic web tools and parsers.


**Example RDF structure:**

.. code-block:: xml

    <rdf:RDF
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:dcterms="http://purl.org/dc/terms/"
      xmlns:ontologizer="https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html#"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

      <!-- Top-level collection -->
      <ontologizer:Collection rdf:about="https://ontolearner.readthedocs.io/benchmarking/benchmark.html">
        <dc:title>OntoLearner Benchmark Ontologies</dc:title>
        <dc:description>This Dublin Core metadata collection describes ontologies benchmarked in OntoLearner. It includes information such as title, creator, format, license, and version.</dc:description>
        <dc:creator>OntoLearner Team</dc:creator>
        <dcterms:license>MIT License</dcterms:license>
        <dcterms:hasVersion>1.4.0</dcterms:hasVersion>
      </ontologizer:Collection>

      <!-- Individual ontology metadata -->
      <ontologizer:Ontology rdf:about="https://ontolearner.readthedocs.io/benchmarking/medicine/ncit.html">
        <dc:identifier>NCIt</dc:identifier>
        <dcterms:title>NCI Thesaurus (NCIt)</dcterms:title>
        <dcterms:description>NCI Thesaurus (NCIt) is a reference terminology that includes broad coverage of the cancer domain...</dcterms:description>
        <dcterms:format>OWL</dcterms:format>
        <dcterms:date>2023-10-19</dcterms:date>
        <dcterms:license>Creative Commons 4.0</dcterms:license>
        <dcterms:source>https://terminology.tib.eu/ts/ontologies/NCIT</dcterms:source>
        <dcterms:subject>Medicine</dcterms:subject>
        <dcterms:subject>Cancer, Oncology</dcterms:subject>
        <dcterms:hasVersion>24.04e</dcterms:hasVersion>
      </ontologizer:Ontology>

    </rdf:RDF>


Properties
-------------------------------------
The following table summarizes the key **Dublin Core metadata properties** captured for each ontology in OntoLearner. It provides a quick overview of the ontology’s identifier, title, description, authorship, format, license, domain, and version information, helping users understand and reference the ontologies consistently.

.. list-table:: **OntoLearner Metadata Properties**
   :header-rows: 0
   :widths: 40 40 40

   * - **Property**
     - **Example**
     - **Description**
   * - ``dc:identifier``
     - NCIt
     - Ontology ID
   * - ``dcterms:title``
     - NCI Thesaurus (NCIt)
     - Ontology full name
   * - ``dcterms:description``
     - NCI Thesaurus (NCIt) is a reference terminology that includes broad coverage of the cancer domain...
     - Detailed ontology description
   * - ``dcterms:creator``
     - NCI
     - Creator / author
   * - ``dcterms:format``
     - OWL
     - Ontology format
   * - ``dcterms:date``
     - 2023-10-19
     - Last updated
   * - ``dcterms:license``
     - Creative Commons 4.0
     - License information
   * - ``dcterms:source``
     - `https://terminology.tib.eu/ts/ontologies/NCIT <https://terminology.tib.eu/ts/ontologies/NCIT>`_
     - Download or reference URL
   * - ``dcterms:subject``
     - Medicine
     - Domain or category
   * - ``dcterms:hasVersion``
     - 24.04e
     - Ontology version

The following represents the benchmark collection info. The `dcterms:hasVersion` represents the library version that the metadata was released.

.. code-block:: xml

	<ontologizer:Collection rdf:about="https://ontolearner.readthedocs.io/benchmarking/benchmark.html">
		<dc:title>OntoLearner Benchmark Ontologies</dc:title>
		<dc:description>This Dublin Core metadata collection describes ontologies benchmarked in OntoLearner. It includes information such as title, creator, format, license, and version.</dc:description>
		<dc:creator>OntoLearner Team</dc:creator>
		<dcterms:license>MIT License</dcterms:license>
		<dcterms:hasVersion>1.4.0</dcterms:hasVersion>
	</ontologizer:Collection>

Exporter
--------------------

``OntoLearnerMetadataExporter`` is included in the OntoLearner library, which you can store the ontology locally.

.. code-block:: python

    from ontolearner import OntoLearnerMetadataExporter

    # Initialize exporter
    exporter = OntoLearnerMetadataExporter()

    # Export metadata to RDF/XML
    exporter.export("ontolearner-metadata.rdf")

The above code outputs:

- **File:** ``ontolearner-metadata.rdf``
- **Format:** Pretty-printed RDF/XML
- **Content:** metadata for each ontology

The top-level collection describes the entire OntoLearner benchmark, while each ontology entry includes detailed metadata using Dublin Core and DCTERMS properties.

.. hint::

	**Namespace Bindings:** The exporter uses the following namespaces in the RDF output:

	- ``dc``: ``http://purl.org/dc/elements/1.1/``
	- ``dcterms``: ``http://purl.org/dc/terms/``
	- ``ontologizer``: ``https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html#``
	- ``rdf``: ``http://www.w3.org/1999/02/22-rdf-syntax-ns#``

.. note::

	- The **Collection resource** always appears first in the RDF/XML output.
	- Individual ontologies are serialized as ``ontologizer:Ontology`` resources.
	- The ``export()`` method automatically reads the OntoLearner library version from the ``VERSION`` file.
	- The RDF/XML output is compatible with standard semantic web tools like **Protégé**, **RDFLib**, and **Apache Jena**.
