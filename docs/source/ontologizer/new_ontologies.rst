New Ontologies
======================

.. sidebar:: Installation:

    Before adding a new ontology, make sure you have OntoLearner `installed <https://ontolearner.readthedocs.io/installation.html>`_, and the ontology file is in a supported format (OWL, RDF, TTL, etc.)

	.. code-block:: bash

		pip install -u OntoLearner

This guide explains how to add new ontologies to the OntoLearner. Adding a new ontology involves creating a Ontologizer (class for the ontology to be imported Programmatically), implementing the necessary methods, and to process and benchmark the ontology.


Create Ontologizer
----------------------



.. sidebar:: Example Ontologizers

    - From medicine domain  `Human Disease Ontology (DOID) <https://github.com/sciknoworg/OntoLearner/blob/main/ontolearner/ontology/medicine.py#L69>`_
    - From biology domain: `Marine Taxonomy and Life Ontology (MarineTLO) <https://github.com/sciknoworg/OntoLearner/blob/main/ontolearner/ontology/biology.py#L106>`_


In OntoLearner, **Ontologizers** are Python classes that represent specific ontologies
and provide a standardized interface for loading, processing, and extracting data
from ontological knowledge bases. These classes serve as the foundation for ontology learning tasks and use-cases.


To create Ontologizer, first, you need to create a class for your ontology that inherits from ``BaseOntology``. This class should be added to the appropriate domain-specific file in the `ontolearner/ontology/ <https://github.com/sciknoworg/OntoLearner/tree/main/ontolearner/ontology>`_ directory.

Here are how to add such a class:

.. code-block:: python

    class MyNewOntology(BaseOntology):
        """
        Description of the ontology - provide a comprehensive overview of what this ontology covers.
        """
        ontology_id = "MyNewOntology"
        ontology_full_name = "My New Comprehensive Ontology (MyNewOntology)"
        domain = "Medicine"  # Choose from existing domains in DOMAINS_DEFINITIONS
        category = "Medical Terminology"
        version = "1.0.0"
        last_updated = "2024-06-01"
        creator = "Your Organization"
        license = "Creative Commons 4.0"
        format = "OWL"  # The file format (OWL, RDF, TTL, etc.)
        download_url = "https://example.com/my-ontology"

Each ontology class inherits from ``BaseOntology`` and defines:

- **Metadata attributes**: ``ontology_id``, ``domain``, ``version``, ``creator``, etc.
- **Format specification**: File format and download location
- **Custom extraction logic**: Domain-specific processing rules (optional)
- **Import handling**: Support for ontologies with external dependencies


.. note::

	If your ontology imports other ontologies, override the ``contains_imports`` method:

	.. code-block:: python

	        # Optional: Override methods if needed
	        def contains_imports(self) -> bool:
	            """Hook: Check if the ontology contains imports."""
	            return True  # Set to True if your ontology imports other ontologies


.. note::

	If your ontology contains specific blank node patterns that need to be filtered out during extraction, override the ``_is_anonymous_id`` method in your ontology class:


	.. code-block:: python

	    def _is_anonymous_id(label: str) -> bool:
	        """Override to handle ontology-specific blank nodes."""
	        # Check the general patterns from the parent class
	        if BaseOntology._is_anonymous_id(label):
	            return True

	        # Add ontology-specific patterns
	        if re.match(r'^PATTERN_[0-9a-f]+$', label):
	            return True

	        return False


.. hint::

	Place your ontology file in the appropriate directory. Here lets say ``ontology_dir`` is the appropiate directory. The directory structure should match the domain of your ontology:

	.. code-block:: text

		ontology_dir/
			└── mynewontology.owl


Ontology Processor
------------------------



To process the ontology and generate benchmarks, you will need to use a dedicated ``Processor`` module within OntoLearner. It will:

1. Loads the ontology
2. Extracts term typings, taxonomic relations, and non-taxonomic relations
3. Calculates metrics
4. Generates documentation

.. code-block:: python

	# import ontology processor!
	from ontolearner import Processor
	# import your ontology!
	from ontolearner.ontology import MyNewOntology

	# 1. Loads the ontology
	# 2. Extracts term typings, taxonomic relations, and non-taxonomic relations
	# 3. Calculates metrics
	# 4. Generates documentation
	processor = Processor()

	processor.process(ontology=MyNewOntology(), ontology_path='ontology_dir/mynewontology.owl')


You can also access the processed ontology via:

.. code-block::  python

	processed_ontology = processor.get_processed_ontology()

	# The processed_ontology` is dictionary with following key values:
	# "ontology": ontology
	# "metrics": {...}
	# "ontology_id": "MyNewOntology"
	# "ontology_full_name": "My New Comprehensive Ontology (MyNewOntology)"
	# "domain": "Medicine"
	# "format": "owl"
	# "processing_time": ...
	# "last_updated": "2024-06-01"
	# "ontology_path": 'ontology_dir/mynewontology.owl',
	# "ontology_data": ...,
	# "documentation": ...

Once this process is done, you might use the `.save_resource` function to check the constructed files and documentations:

.. code-block:: python

	processor.save_resource(output_dir="my-ontology")

This will results in a ontology directory with following structure:

.. code-block:: text

	my-ontology/
		└──MyNewOntology/
			└──mynewontology.rst
			└──mynewontology.owl
			└──term_typings.json
			└──type_taxonomies.json
			└──type_non_taxonomic_relations.json

Review the generated data and documentation. Then proceed with submiting your merge request to the library. We will take care of the updating `🤗 HuggingFace repository <https://huggingface.co/collections/SciKnowOrg/ontolearner-benchmarking-6823bcd051300c210b7ef68a>`_ and documntation webpage and release of the library with your ontology!

.. note::

	You **DO NOT** need to submit ontologies and files within `Merge Request <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request>`_. We will create the resource from your code and will update the both website and 🤗 HuggingFace.


Help
---------------

**Custom Extraction Logic.** If your ontology requires custom extraction logic, you can override the extraction methods within Ontologizer:

- ``extract_term_typings``
- ``extract_type_taxonomies``
- ``extract_type_non_taxonomic_relations``

For example:

.. code-block:: python

    def extract_term_typings(self) -> List[TermTyping]:
        """Custom implementation for extracting term typings."""
        # Your custom implementation
        pass


**Troubleshooting**: Common issues when adding new ontologies:

1. **Ontology file not found**: Ensure the ontology file is in the correct location and has the correct name.
2. **Parsing errors**: Check that the ontology file is in the format specified in the ontology class.
3. **Empty datasets**: If the extraction produces empty datasets, check if the ontology uses standard RDF/OWL constructs or if it needs custom extraction logic.
4. **Blank node issues**: If you see strange identifiers in your extracted data, you may need to add custom blank node patterns to filter them out.
