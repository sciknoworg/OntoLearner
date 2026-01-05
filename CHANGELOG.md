## Changelog

### v1.4.11 (January 5, 2026)
- Add `text2onto` component for challenge learners with their documentation.
- Code refactoring
- OS compatibility CI/CD

### v1.4.10 (December 8, 2025)
- add complexity score
- add documentation for metrics
- bug fixes in Ontologizer

### v1.4.9 (December 8, 2025)
- add retriever collection
- add documentation for retrievers
- minor bug fixings in docs
- add unittest for retrievers
- add new requirements (`gensim`)

### v1.4.8 (December 3, 2025)
- add alexbeck, rwthdbis, sbunlp, and skhnlp learners
- add documentation for learners
- minor bug fixings

### v1.4.7 (October 1, 2025)
- add custom LLM based learner
- add Falcon-H and Mistral-Small custom AutoLLMs.
- Add custom LLm documentations.
- Minor bug fix and improvements in documentation and code.

### v1.4.6 (September 22, 2025)
- add type annotation to metrics
- add minor fix to retriever taxonomy discovery
- add count metrics in evaluation.

### v1.4.5 (September 16, 2025)
- add batch retriever feature to `AutoRetrieverLearner`


### v1.4.4 (September 9, 2025)
- add `trust_remote_code=True` for retrievers like Nomic-AI

### v1.4.3 (September 7, 2025)
- Update dependencies
- fix bug in learner
- cosmetic fix to the docs

### v1.4.2 (September 1, 2025)
- fix dependency issue for torch and transformers.
- update maintenance plan

### v1.4.1 (August 22, 2025)
- added ontolearner-metadata CI/CD based build.

### v1.4.0 (August 22, 2025)
- added dublin core metadata exporter
- added ontolearner metadata documentation
- added `VERSION` file for versioning

### v1.3.1 (August 13, 2025)
- `Processor` module is operational. Fixed with ease of use principles.
- The huggingface readme files template are updated.
- Documentation website benchmark pages are updated.
- Cosmetic fixes.
- Remove static methods feature from Ontologizer for smooth development.
- add `openpyxl` dependency for xlsx load.

### v1.3.0 (July 14, 2025)
- Add verbose for logging at train-test splits
- High-level encapsulation of learners: LLM, retriever, and rag
- Update pipeline to a newer version
- Optimize code
- Refactor examples
- Delete dummy scripts from the script dir
- Parameter custmization
- Add AutoOntology feature
- Extensive update on documentation
- Update Readme
- Add Unittest
- Add package references in the documentation website

### v1.2.1 (June 20, 2025)
- fix toml packages reference
- add print functionality to ontologizer

### v1.2.0 (June 20, 2025)
- adding new ontology (Framester)
- enhance documentation
- add test CI/CD
- update automatic push-to-hub functionality
- update dependencies.
- upgrade ontology load functionality
- update maintenance plan

### v1.1.2 (June 11, 2025)
- add PKO ontology
- add push-to-hub interface
- refactor documentation.

### v1.1.1 (May 27, 2025)
- add HF documentation
- add license headers
- refactor documentations
- improve hf layout
- add examples

### v1.1.0 (May 21, 2025)
- Version changes
- Refactor documentations
- Add Readme
- Fix learner model and pipelines

### v1.0.1 (May 13, 2025)
- Fix typo mistake in CITATION.cf

### v1.0.0 (May 13, 2025)
- Added learner models: LLM, Retrieval, and RAG models.
- Machine Learning Helpers: train-test-split, evaluation metrics, visualizations.
- Added examples for learner models.
- Finalized documentation pages.


### v0.5.0 (May 8, 2025)
- Added text2onto documentations
- Bug fixes to the ontology module
- Added HF integration

### v0.4.0 (May 2, 2025)
- Added text2onto module
- Bug fixings to the text2onto new module
- Added text2onto documentation page
- Added minor necessary files to the repo.

### v0.3.0 (April 24, 2025)
- Added full ontologies
- Automated documentation generation
- Added ontology evaluation metrics
- Added initial text2onto module
- Code refactoring
- Bug fixes

### v0.2.0 (April 10, 2025)
- Added new ontologies
- Added documnetations to new ontologies
- Fixed domains according to [#205](https://github.com/sciknoworg/OntoLearner/issues/205)

### v0.1.0 (March 17, 2025)
Features
- Framework for processing, analyzing, and visualizing diverse ontologies.
- Support for over 100 domain-specific ontologies including scientific, scholarly, and domain-specific knowledge bases
- Comprehensive ontology processing pipeline with extraction of term typings, taxonomic, and non-taxonomic relations
- Graph-based analysis with metrics for topology and dataset characteristics
- Visualization tools for ontology structure and metrics presentation

Implementation
- RDF/OWL parsing support with comprehensive import resolution
- NetworkX integration for graph algorithm implementation
- Modular architecture with extensible base classes for custom ontology implementations
- Pydantic data models for robust data validation and serialization
- Built-in benchmarking and metrics collection

Documentation
- Usage examples for each supported ontology
- Comprehensive metrics documentation
- RST-based documentation with auto-generated API references
