# OntoLearner Maintenance Plan

The OntoLearner library is designed to facilitate ontology learning and reuse. To ensure that OntoLearner remains a reliable and relevant tool for the community, we establish this Maintenance Plan to outline the ongoing maintenance efforts, the roles involved, and the strategies for addressing evolving user needs.  This library is released under [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
, a permissive open-source license that allows for community contributions, reuse, and modification. A persistent [![DOI](https://zenodo.org/badge/913867999.svg)](https://doi.org/10.5281/zenodo.15399773) is assigned via Zenodo to ensure permanent referencing of the latest stable release.  Release versions will be tagged on GitHub, with versioning to track major, minor, and patch updates. The release will be pushed to the [OntoLearner at PyPI](https://pypi.org/project/OntoLearner/). The current version of OntoLearner is ![PyPI version](https://badge.fury.io/py/OntoLearner.svg).

## 1. Objectives & Responsibilities

The primary goals of the OntoLearner maintenance objectives are to:
- Ensure long-term availability and functionality of the library by addressing and fix bugs and issues as they arise.
- Continuously add Aligner models and extend models within the OntoLearner.
- Incorporate user feedback and adapt to evolving research trends in ontology learning.
- Maintain up-to-date documentation to support ease of use and understanding.
- Regularly review and update dependencies to maintain compatibility with the latest technology and standards.

A core team will be responsible for the ongoing maintenance of OntoLearner, including:
- **Lead Maintainers**: Oversee all maintenance activities, ensure the direction aligns with the project's vision, and handle critical issues.
  - [Dr. Jennifer D'Souza](https://sites.google.com/view/jen-web) and [Hamed Babaei Giglou](https://hamedbabaei.github.io/) – Project Lead – Responsible for the overall vision, maintenance activities, and coordination of the library’s development.
  - [Prof. Dr. Sören Auer](https://www.tib.eu/en/research-development/research-groups-and-labs/data-science-and-digital-libraries/staff/soeren-auer) – Project Supervisors and Principal Investigators (PI) – Responsible for guiding ideation, refining ideas, and defining the project's high-level direction to align the library's goals with broader academic and research objectives.
- **Assistants**:
  - [Krishna Rani](www.linkedin.com/in/krishna-rani-thakur-5b77b9150) - Assists with activities such as maintaining the codebase for the smooth operation of the project.
- **Alumni**:
  - [Andrei Aionei](https://www.linkedin.com/in/andreiaioanei/) – Andrei was project Senior Software Engineer – Responsible for maintenance activities and the library’s development.

## 2. Current Ongoing Maintenance and Plans

A roadmap for new features and improvements, ensuring the library evolves in response to user needs and feedback is presented as follows. This list will be updated regularly as we explore the variety of works within the ontology alignment field to ensure the diverse methods within the library.

| Category   | Description                                                                                                                                                                                                 |                          Status                           |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------:|
|Ontologizer| Adding more ontologies to the OntoLearner                                                                                                                                                                   | InProgress|
| Reasoning  | Integration of reasoning-oriented prompt evaluation tasks to test LLM capabilities in generating consistent and logically valid ontological structures (e.g., subclass chains, disjointness, transitivity). |                          TODO                             |
| Agentic    | Support for agent-based extensions using platforms like [CrewAI](https://github.com/crewAIInc/crewAI) to enable autonomous, multi-step ontology engineering workflows coordinated through modular agents.   |                          TODO                             |
|Documentation| Adding more documentation and tutorials                                                                                                                                                                     | InProgress|
|Testing| Adding unittest to support different stages of modularization                                                                                                                                               | InProgress|
|Learner| Incorporating more learner models. Including those from LLMs4OL challenge                                                                                                                                   | InProgress|
|Reasoning| Adding reasoning techniques                                                                                                                                                                                 | To-Do|
|...| ...                                                                                                                                                                                                         |...|

> **If you are willing to have your Ontology Learning model or feature within OntoLearner don't hesitate to contact us via [GitHub Issues](https://github.com/sciknoworg/ontolearner/issues) or via email to [hamed.babaei@tib.eu](mailto:hamed.babaei@tib.eu)**.

## 3. Maintenance Regulations
The following activities will be performed regularly:
- **Code Quality**:
  - Enforce PEP 8 compliance and code consistency using `pre-commit` hooks with `ruff` for linting and formatting.
  - Run pre-commit checks regularly to maintain code quality and prevent style violations before commits.
  - Perform continuous code refactoring to improve readability and reduce technical debt.
- **Version Control**:
  - During the development or contribution we obligated to use Git with clear commit messages following best practices.
  - We follow semantic versioning for the releases (e.g., v1.0.0 for the first stable release).
  - OntoLearner Utilize GitHub **CI/CD** for automated ReadTheDocs deployment on every push to the main branch.
  - Moreover, the PyPI release is automated for each versioning tag ensuring easy distribution.
  - Each release includes (and should contain) proper documentation and a detailed in the **[CHANGELOG.md](CHANGELOG.md)** for new features, bug fixes, and breaking changes.
- **Release Cycle**:
  - **Major Releases**: Major feature updates or breaking changes will be released every 6 months. These releases will introduce new features, remove deprecated functionality, or make significant changes to the architecture.
  - **Minor Releases**: Regular updates that add new features or improvements will be released every month.
  - **Patch Releases**: Bug fixes, security patches, and minor adjustments will be released as necessary, with a goal of addressing critical issues within 2-3 weeks of identification.
- **Documentation**
  - Each new ontology should include a documentation guide for users to quickly use that model within the OntoLearner on real-world datasets.
  - User documentation aim is to provide detailed information for each class and method for users to easily understand and apply.
  - Code-level documentation is a "must" for the project as we use `Sphinx` to generate API documentation from docstrings.
- **Compatibility Checks**:
  - Regularly monitoring and updating dependencies (e.g., `rdflib`, `owlready2`, `transformers`) to ensure compatibility with the latest Python versions and security patches.
  - Regularly test compatibility with Python 3.10 and newer versions (e.g., Python 3.11, 3.12).
- **Security Management**:
  - The sensitive data such as API keys or passwords are not allowed to be hard-coded in the repository. But allowed to use feed as an argument while using specific models.
  - Each merge request will be assigned for code reviews focusing on security, especially when handling user data or integrating with external services.


## 4. Community Engagement
- We use [GitHub Issues](https://github.com/sciknoworg/ontolearner/issues) to track bugs, feature requests, and enhancements, ensuring critical issues get a response within **48 hours**.
- Contribution guidelines are outlined in **[CONTRIBUTING.md](CONTRIBUTING.md)**, detailing what contributions can be made, code standards, and PR submission processes.

- OntoLearner Code of Conduct is available at **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** to foster a welcoming and inclusive environment for community engagement.


For any inquiries for issue reporting, or long-term support, please feel free to contact the maintainer at **[hamed.babaei@tib.eu](mailto:hamed.babaei@tib.eu)**.
