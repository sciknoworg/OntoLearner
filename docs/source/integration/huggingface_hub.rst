HuggingFace Integration
==========================

Accessing Ontologies via Hub
-----------------------------
OntoLearner ontologies are available on HuggingFace Hub for easy access and integration:

.. code-block:: python

    from huggingface_hub import snapshot_download

    # Download specific ontology
    ontology_path = snapshot_download(
        repo_id="TIB/ontologies",
        repo_type="dataset",
        allow_patterns=f"CSO.3.4.owl"
    )

Available Ontologies
--------------------
.. list-table:: Available Ontologies on Hub
   :header-rows: 1
   :widths: 20 20 20 40

   * - Domain
     - Name
     - Version
     - HF Path
   * - Computer Science
     - CSO
     - 3.4
     - TIB/ontologies/CSO.3.4.owl
   * - Emotions
     - MFOEM
     - 2025-01
     - TIB/ontologies/mfoem.owl
   * - Biology
     - Plant
     - 2024
     - TIB/ontologies/plant.owl

LLM Integration Examples
-------------------------

Fine-tuning
^^^^^^^^^^^
.. code-block:: python

    from ontolearner.utils.llm_utils import prepare_ontology_for_finetuning

    # Prepare ontology data for fine-tuning
    train_data = prepare_ontology_for_finetuning(
        ontology_name="CSO",
        task_type="taxonomy",  # or "typing" or "relations"
        format="instruction"  # or "completion"
    )

Inference
^^^^^^^^^
.. code-block:: python

    from ontolearner.utils.llm_utils import load_ontology_context

    # Load ontology as context for LLM
    context = load_ontology_context(
        domain="computer_science",
        task="term_typing"
    )
