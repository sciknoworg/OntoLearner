New Ontologies
======================

This guide explains how to add new ontologies to the OntoLearner. Adding a new ontology involves creating a class for the ontology, implementing the necessary methods,
and to process and benchmark the ontology.

.. hint::

    **Add New Ontology Script**: Use `add_new_ontology.py <https://github.com/sciknoworg/OntoLearner/blob/main/scripts/add_new_ontology.py>`_ script for processing and benchmarking your ontology.

.. note::

    Before adding a new ontology, make sure you have OntoLearner `installed <https://ontolearner.readthedocs.io/installation.html>`_, and the ontology file is in a supported format (OWL, RDF, TTL, etc.)

Step 1: Create Ontologizer
--------------------------
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

        # Optional: Override methods if needed
        def contains_imports(self) -> bool:
            """Hook: Check if the ontology contains imports."""
            return True  # Set to True if your ontology imports other ontologies

        # Optional: Add custom blank node patterns if needed
        @staticmethod
        def _is_anonymous_id(label: str) -> bool:
            """Override to handle ontology-specific blank nodes."""
            # Check the general patterns from the parent class
            if BaseOntology._is_anonymous_id(label):
                return True
            # Add ontology-specific patterns
            if re.match(r'^MY_[0-9]+$', label):  # Example pattern
                return True
            return False

Each ontology class inherits from ``BaseOntology`` and defines:

- **Metadata attributes**: ``ontology_id``, ``domain``, ``version``, ``creator``, etc.
- **Format specification**: File format and download location
- **Custom extraction logic**: Domain-specific processing rules (optional)
- **Import handling**: Support for ontologies with external dependencies

Step 2: Place the Ontology File
----------------------------------
Place your ontology file in the appropriate directory under ``data/ontologies/``.
The directory structure should match the domain of your ontology:

.. code-block:: text

    data/
    └── ontologies/
        └── medicine/
            └── mynewontology.owl

The file should be named according to the pattern: ``<ontology_id>.lower().<format>.lower()``.

Step 3: Process the Ontology
-------------------------------
To process the ontology and generate benchmarks, you'll use the ``add_new_ontology.py`` script. This script:

1. Loads the ontology
2. Extracts term typings, taxonomic relations, and non-taxonomic relations
3. Calculates metrics
4. Generates documentation
5. Exports metrics to Excel

Edit the ``scripts/add_new_ontology.py`` file to include your new ontology in the list of ontologies to process:

.. code-block:: python

    ontologies = [
        # Other ontologies...

        # Medicine Ontologies
        MyNewOntology(),

        # Other ontologies...
    ]

Then run the script:

.. code-block:: bash

    cd scripts
    python add_new_ontology.py

The script will:

1. Load your ontology from the specified path
2. Process the ontology to extract datasets
3. Calculate metrics
4. Generate a documentation file in ``docs/source/benchmarking/<domain>/``
5. Save the extracted datasets to ``data/datasets/<domain>/<ontology_id>/``
6. Update the metrics Excel file in ``data/metrics/metrics.xlsx``


Step 4: Review the Generated Documentation
---------------------------------------------

After running the script, check the generated documentation file at ``docs/source/benchmarking/<domain>/<ontology_id>.rst``.
This file contains:

1. Overview of the ontology
2. Graph metrics
3. Knowledge coverage
4. Hierarchical metrics
5. Breadth metrics
6. Dataset statistics
7. Usage example

Make any necessary adjustments to the documentation to ensure it accurately represents your ontology.


Step 5: Update the Benchmark Index
--------------------------------------

If you're adding an ontology to a new domain that doesn't exist yet, you'll need to update the ``docs/source/benchmarking/benchmark.rst`` file to include the new domain and ontology.

Handling Special Cases
------------------------

**Blank Node Patterns**

If your ontology contains specific blank node patterns that need to be filtered out during extraction, override the ``_is_anonymous_id`` method in your ontology class:

.. code-block:: python

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle ontology-specific blank nodes."""
        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        # Add ontology-specific patterns
        if re.match(r'^PATTERN_[0-9a-f]+$', label):
            return True

        return False


**Ontology Imports**


If your ontology imports other ontologies, override the ``contains_imports`` method:

.. code-block:: python

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True

**Custom Extraction Logic**

If your ontology requires custom extraction logic, you can override the extraction methods:

- ``extract_term_typings``
- ``extract_type_taxonomies``
- ``extract_type_non_taxonomic_relations``

For example:

.. code-block:: python

    def extract_term_typings(self) -> List[TermTyping]:
        """Custom implementation for extracting term typings."""
        # Your custom implementation
        pass


Troubleshooting
--------------------
Common issues when adding new ontologies:

1. **Ontology file not found**: Ensure the ontology file is in the correct location and has the correct name.
2. **Parsing errors**: Check that the ontology file is in the format specified in the ontology class.
3. **Empty datasets**: If the extraction produces empty datasets, check if the ontology uses standard RDF/OWL constructs or if it needs custom extraction logic.
4. **Blank node issues**: If you see strange identifiers in your extracted data, you may need to add custom blank node patterns to filter them out.

For more complex issues, refer to the OntoLearner documentation or open an issue on the GitHub repository.
