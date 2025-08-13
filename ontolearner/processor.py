# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pip install langchain

import logging
import time
import pandas as pd

import shutil
import tempfile
from pathlib import Path
from typing import Union, Any, Dict
from jinja2 import Template
from huggingface_hub import HfApi, Repository
from huggingface_hub.errors import RepositoryNotFoundError


from .base import BaseOntology
from .data_structure import OntologyMetrics, OntologyData, DatasetMetrics, TopologyMetrics
from .tools import Analyzer
from .utils import io


logger = logging.getLogger(__name__)

# Domain definitions for README generation
DOMAIN_DEFINITIONS = {
    "agriculture": "Ontologies about farming systems, crops, food production, and agricultural vocabularies.",
    "arts_and_humanities": "Ontologies that describe music, iconography, cultural artifacts, and humanistic content.",
    "biology_and_life_sciences": "Ontologies about biological entities, systems, organisms, and molecular biology.",
    "chemistry": "Ontologies describing chemical entities, reactions, methods, and computational chemistry models.",
    "ecology_and_environment": "Ontologies about ecological systems, environments, biomes, and sustainability science.",
    "education": "Ontologies describing learning content, educational programs, competencies, and teaching resources.",
    "events": "Ontologies for representing events, time, schedules, and calendar-based occurrences.",
    "finance": "Ontologies describing economic indicators, e-commerce, trade, and financial instruments.",
    "food_and_beverage": "Ontologies related to food, beverages, ingredients, and culinary products.",
    "general_knowledge": "Broad-scope ontologies and upper vocabularies used across disciplines for general-purpose semantic modeling.",
    "geography": "Ontologies for modeling spatial and geopolitical entities, locations, and place names.",
    "industry": "Ontologies describing industrial processes, smart buildings, manufacturing systems, and equipment.",
    "law": "Ontologies dealing with legal processes, regulations, and rights (e.g., copyright).",
    "library_and_cultural_heritage": "Ontologies used in cataloging, archiving, and authority control of cultural and scholarly resources.",
    "materials_science_and_engineering": "Ontologies related to materials, their structure, properties, processing, and engineering applications.",
    "medicine": "Ontologies covering clinical knowledge, diseases, drugs, treatments, and biomedical data.",
    "news_and_media": "Ontologies that model journalism, broadcasting, creative works, and media metadata.",
    "scholarly_knowledge": "Ontologies modeling the structure, process, and administration of scholarly research, publications, and infrastructure.",
    "social_sciences": "Ontologies for modeling societal structures, behavior, identity, and social interaction.",
    "units_and_measurements": "Ontologies defining scientific units, quantities, dimensions, and observational models.",
    "upper_ontology": "Foundational ontologies that provide abstract concepts like objects, processes, and relations.",
    "web_and_internet": "Ontologies that model web semantics, linked data, APIs, and online communication standards."
}

DOMAIN_DESCRIPTIONS = {
    "agriculture": "The agriculture domain encompasses the structured representation and systematic study of farming systems, crop cultivation, livestock management, and food production processes. It focuses on the development and utilization of comprehensive agricultural vocabularies and taxonomies to facilitate precise knowledge representation and interoperability across diverse agricultural practices and technologies. This domain is pivotal in advancing sustainable agricultural practices, enhancing food security, and supporting decision-making through the integration of scientific, economic, and environmental data.",
    "arts_and_humanities": "The arts and humanities domain encompasses ontologies that systematically represent and categorize the diverse aspects of human cultural expression, including music, visual arts, historical artifacts, and broader humanistic studies. This domain plays a crucial role in knowledge representation by providing structured frameworks that facilitate the organization, retrieval, and analysis of cultural and artistic information, thereby enhancing interdisciplinary research and digital scholarship. Through precise modeling of complex cultural phenomena, these ontologies contribute to the preservation and dissemination of human heritage in the digital age.",
    "biology_and_life_sciences": "The biology and life sciences domain encompasses the structured representation and categorization of knowledge related to biological entities, processes, and systems, ranging from molecular and cellular levels to complex organisms and ecosystems. This domain plays a critical role in facilitating data interoperability, integration, and retrieval across diverse biological disciplines, thereby advancing research and discovery. By providing a formalized framework for understanding biological concepts and their interrelations, it supports the development of computational models and enhances the precision of scientific communication.",
    "chemistry": "The chemistry domain encompasses the structured representation and formalization of chemical knowledge, including entities, reactions, processes, and methodologies. It plays a critical role in knowledge representation by enabling the integration, sharing, and computational analysis of chemical data across diverse subfields such as organic, inorganic, physical, and computational chemistry. This domain facilitates the advancement of scientific research and innovation by providing a standardized framework for the precise and interoperable exchange of chemical information.",
    "ecology_and_environment": "The ecology and environment domain encompasses the structured representation of knowledge pertaining to ecological systems, diverse environmental contexts, biomes, and the principles of sustainability science. This domain is pivotal in facilitating the integration, sharing, and analysis of complex environmental data, thereby advancing our understanding of ecological interactions and promoting informed decision-making for sustainable development. By providing a formalized framework, it supports interdisciplinary research and policy-making aimed at addressing global environmental challenges.",
    "education": "The education domain encompasses ontologies that systematically represent and organize knowledge related to learning content, educational programs, competencies, and teaching resources. This domain plays a critical role in facilitating semantic interoperability and enhancing the precision of information retrieval and management within educational contexts. By providing a structured framework for the representation of educational concepts and relationships, it supports the development of intelligent systems that can effectively process and utilize educational data.",
    "events": "The events domain encompasses the structured representation and semantic modeling of occurrences in time, including their temporal, spatial, and contextual attributes. This domain is pivotal in knowledge representation as it facilitates the interoperability and integration of event-related data across diverse systems, enabling precise scheduling, planning, and historical analysis. By providing a framework for understanding and linking events, this domain supports advanced applications in areas such as artificial intelligence, information retrieval, and decision support systems.",
    "finance": "The finance domain encompasses the structured representation of concepts and relationships pertaining to economic indicators, financial markets, investment vehicles, and monetary transactions. It focuses on the precise modeling of financial instruments, trade mechanisms, and e-commerce processes to facilitate interoperability and data exchange across diverse financial systems. This domain is crucial for advancing knowledge representation, enabling sophisticated analysis, decision-making, and automation in financial services.",
    "food_and_beverage": "The food and beverage domain ontologies encompasses the structured representation and categorization of knowledge related to food items, beverages, their ingredients, and culinary processes. This domain plays a critical role in facilitating semantic interoperability, data integration, and advanced information retrieval across diverse applications, including gastronomy, nutrition, and food science. By providing a formalized framework, it enables precise communication and analysis within and across disciplines, enhancing both academic research and practical applications in the food and beverage industry.",
    "general_knowledge": "The general knowledge domain ontologies encompasses broad-scope ontologies and upper vocabularies designed for cross-disciplinary semantic modeling and knowledge representation. This domain is pivotal in facilitating interoperability and data integration across diverse fields by providing a foundational framework for organizing and linking information. Its significance lies in enabling the seamless exchange and understanding of knowledge across varied contexts, thereby supporting advanced data analysis, information retrieval, and decision-making processes.",
    "geography": "The geography domain encompasses the structured representation and analysis of spatial, environmental, and geopolitical phenomena, focusing on the precise modeling of physical locations, territorial boundaries, and place names. This domain is pivotal in knowledge representation as it facilitates the integration and interoperability of geographic information across diverse systems, enabling advanced spatial reasoning and decision-making. By providing a formal framework for understanding the complex relationships between geographic entities, this domain supports a wide range of applications, from urban planning to environmental monitoring.",
    "industry": "The industry domain encompasses ontologies that systematically represent and model the complex structures, processes, and interactions within industrial settings, including manufacturing systems, smart buildings, and equipment. This domain is pivotal in advancing knowledge representation by enabling the integration, interoperability, and automation of industrial processes, thereby facilitating improved efficiency, innovation, and decision-making. Through precise semantic frameworks, it supports the digital transformation and intelligent management of industrial operations.",
    "law": "The law domain encompasses ontologies that systematically represent the complex structures and interrelations of legal concepts, processes, regulations, and rights. This domain is pivotal in knowledge representation as it facilitates the formalization and interoperability of legal information, enabling precise reasoning and decision-making across diverse legal systems. By capturing the intricacies of legal language and practice, these ontologies support the automation and enhancement of legal services and research.",
    "library_and_cultural_heritage": "The library and cultural heritage domain encompasses ontologies that facilitate the systematic organization, cataloging, and preservation of cultural and scholarly resources. This domain plays a critical role in knowledge representation by ensuring consistent metadata standards, enabling interoperability across diverse information systems, and supporting the discovery and retrieval of cultural assets. It is integral to maintaining the integrity and accessibility of cultural heritage and scholarly communication in both digital and physical environments.",
    "materials_science_and_engineering": "Materials Science and Engineering is a multidisciplinary domain that focuses on the study and application of materials, emphasizing their structure, properties, processing, and performance in engineering contexts. This field is pivotal for advancing knowledge representation, as it integrates principles from physics, chemistry, and engineering to innovate and optimize materials for diverse technological applications. By systematically categorizing and modeling material-related data, this domain facilitates the development of new materials and enhances the understanding of their behavior under various conditions.",
    "medicine": "The domain of medicine encompasses the structured representation and systematic organization of clinical knowledge, including the classification and interrelation of diseases, pharmacological agents, therapeutic interventions, and biomedical data. This domain is pivotal for advancing healthcare research, facilitating interoperability among medical information systems, and enhancing decision-making processes through precise and comprehensive knowledge representation. By employing ontologies, this domain ensures a standardized and semantically rich framework that supports the integration and analysis of complex biomedical information.",
    "news_and_media": "The news and media domain encompasses ontologies that systematically represent the structures, processes, and metadata associated with journalism, broadcasting, and creative media works. This domain is pivotal in knowledge representation as it facilitates the organization, retrieval, and analysis of media content, enabling interoperability and semantic understanding across diverse platforms and formats. By providing a structured framework, these ontologies enhance the precision and efficiency of information dissemination and consumption in the digital age.",
    "scholarly_knowledge": "The scholarly knowledge domain encompasses ontologies that systematically represent the intricate structures, processes, and governance mechanisms inherent in scholarly research, academic publications, and the supporting infrastructure. This domain is pivotal in facilitating the organization, retrieval, and dissemination of academic knowledge, thereby enhancing the efficiency and transparency of scholarly communication. By providing a formalized framework for knowledge representation, it supports interoperability and integration across diverse research disciplines and platforms.",
    "social_sciences": "The social sciences domain encompasses ontologies that systematically represent and model the complex structures, behaviors, identities, and interactions inherent in human societies. This domain is pivotal for advancing knowledge representation by providing a structured framework to analyze and interpret social phenomena, facilitating interdisciplinary research and enabling the integration of diverse data sources. Through precise semantic modeling, it enhances our understanding of social dynamics and supports the development of applications that address societal challenges.",
    "units_and_measurements": "The units and measurements domain ontologies encompasses the formal representation and standardization of scientific units, quantities, dimensions, and the models used for their observation and analysis. This domain is crucial for ensuring consistency and interoperability in scientific data exchange, enabling precise communication and computation across diverse fields. By providing a structured framework for understanding and utilizing measurement concepts, it plays a vital role in advancing research, technology, and data-driven decision-making.",
    "upper_ontology": "Upper ontology, also known as a foundational ontology, encompasses a set of highly abstract, domain-independent concepts that serve as the building blocks for more specialized ontologies. These ontologies provide a structured framework for representing fundamental entities such as objects, processes, and relations, facilitating interoperability and semantic integration across diverse domains. By establishing a common vocabulary and set of principles, upper ontologies play a crucial role in enhancing the consistency and coherence of knowledge representation systems.",
    "web_and_internet": "The web and internet domain encompasses ontologies that articulate the structure and semantics of web technologies, including the intricate relationships and protocols that underpin linked data, web services, and online communication standards. This domain is pivotal in advancing knowledge representation by enabling the seamless integration and interoperability of diverse data sources, thereby facilitating more intelligent and dynamic web interactions. Through precise modeling of web semantics, it supports the development of robust frameworks for data exchange and enhances the semantic web's capacity to deliver contextually relevant information."
}

class Processor:
    """
    Handles the complete ontology processing pipeline.

    This class orchestrates the entire ontology processing workflow including:
    - Loading ontologies from files
    - Extracting data and building graphs
    - Analyzing ontology metrics
    - Generating documentation
    - Saving datasets and metrics
    """

    def __init__(self):
        """
        Initialize the Processor with directory paths and configuration.
        """
        self.analyzer = Analyzer()
        self.processed_ontology = None

    def __call__(self, ontology: BaseOntology, ontology_path: Union[str, Path], output_dir: str) -> Dict[str, Any]:
        self.process(ontology, ontology_path)
        self.save_resource(output_dir)
        return self.get_processed_ontology()

    def process(self, ontology: BaseOntology, ontology_path: Union[str, Path]) -> None:
        """
        Process a single ontology through the complete pipeline.

        This method performs the complete processing workflow for an ontology:
        1. Loads the ontology from the specified path
        2. Extracts data and builds the graph representation
        3. Analyzes the ontology to compute metrics
        4. Saves extracted datasets to files
        5. Generates documentation
        6. Records processing time and metrics

        Args:
            ontology (BaseOntology): The ontology instance to process
            ontology_path (Union[str, Path]): Path to the ontology file

        Returns:
            OntologyMetrics: Computed metrics for the ontology

        Raises:
            ValueError: If the ontology file is not found
            Exception: If any step in the processing pipeline fails
        """
        start_time = time.time()
        if not Path(ontology_path).exists():
            raise ValueError(f"Ontology file not found: {ontology_path}")

        ontology.load(str(ontology_path))
        # ontology.load()

        data: OntologyData = ontology.extract()
        ontology.build_graph()

        metrics = self.analyzer(ontology)

        end_time = time.time()
        processing_time = end_time - start_time

        self.processed_ontology = {
            "ontology": ontology,
            "metrics": metrics,
            "ontology_id": ontology.ontology_id,
            "ontology_full_name": ontology.ontology_full_name,
            "domain": ontology.domain,
            "format": ontology.format.lower(),
            "processing_time": processing_time,
            "last_updated": ontology.last_updated,
            "ontology_path": ontology_path,
            "ontology_data": data,
            "documentation": self.build_documentation(ontology, metrics)
        }
        logger.log(level=20, msg=f"Processing {ontology.ontology_id} ontology is done!")

    def get_processed_ontology(self):
        return self.processed_ontology

    def save_resource(self, output_dir: str, show_logs: bool=False, processed_ontology: Dict[str, Any] = None) -> None:
        """
        Save extracted datasets to JSON files.

        Creates domain-specific directories and saves the three main dataset types:
        - term_typings.json: Term to type mappings
        - type_taxonomies.json: Taxonomic relations
        - type_non_taxonomic_relations.json: Non-taxonomic relations

        Args:
            data (OntologyData): Extracted ontology data
            ontology (BaseOntology): The ontology instance
        """
        if processed_ontology is None:
            processed_ontology = self.processed_ontology
        ontology_dir = Path(f"{output_dir}/{processed_ontology['ontology_id'].lower()}")
        ontology_dir.mkdir(parents=True, exist_ok=True)

        # Store the read-the-doc page in documentation page and output dir path!
        # domain_dir = Path(f"docs/source/benchmarking/{processed_ontology['domain'].lower().replace(' ', '_')}")
        #
        # with open(domain_dir / f"{processed_ontology['ontology_id'].lower()}.rst", "w", encoding="utf-8") as f:
        #     f.write(processed_ontology['documentation'])
        #
        # if show_logs:
        #     logger.log(level=20, msg=f"The read-the-doc page in documentation is created for ontology!")

        with open(ontology_dir / f"{processed_ontology['ontology_id'].lower()}.rst", "w", encoding="utf-8") as f:
            f.write(processed_ontology['documentation'])

        if show_logs:
            logger.log(level=20, msg="The documentation page is added to the output dir!")

        # Store the ontology in given dir!
        shutil.copy2(processed_ontology['ontology_path'], ontology_dir/f"{processed_ontology['ontology_id'].lower()}.{processed_ontology['ontology_path'].split('.')[-1]}")

        if show_logs:
            logger.log(level=20, msg="The raw ontology itself added to the output dir!")

        # Store the ontological data
        for dataset_type in ['term_typings', 'type_taxonomies', 'type_non_taxonomic_relations']:
            save_path = ontology_dir / f"{dataset_type}.json"
            io.save_json(processed_ontology['ontology_data'].model_dump()[dataset_type], save_path)
        if show_logs:
            logger.log(level=20, msg="The ontological data added to the output dir!")
            logger.log(level=20, msg=f"The {ontology_dir} is created and data is stored!")

    def build_documentation(self, ontology: BaseOntology, metrics: OntologyMetrics):
        """
        Generate RST documentation from Jinja2 template.

        Creates comprehensive documentation for the ontology including:
        - Metadata (name, domain, version, etc.)
        - Graph metrics (nodes, edges, depth, breadth)
        - Knowledge coverage (classes, individuals, properties)
        - Dataset statistics
        - Usage examples

        Args:
            ontology (BaseOntology): The ontology instance
            metrics (OntologyMetrics): Computed metrics for the ontology
        """
        documentation_template = Template("""{{ ontology_name }}
==============================================================================

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - {{ domain }}
       * - **Category**
         - {{ category }}
       * - **Current Version**
         - {{ version }}
       * - **Last Updated**
         - {{ last_updated }}
       * - **Creator**
         - {{ creator }}
       * - **License**
         - {{ license }}
       * - **Format**
         - {{ format }}
       * - **Download**
         - `Download {{ ontology_name }} <{{ download_url }}>`_

{{ description }}

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - {{ total_nodes }}
        * - **Total Edges**
          - {{ total_edges }}
        * - **Root Nodes**
          - {{ root_nodes }}
        * - **Leaf Nodes**
          - {{ leaf_nodes }}
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - {{ num_classes }}
        * - **Individuals**
          - {{ num_individuals }}
        * - **Properties**
          - {{ num_properties }}

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - {{ max_depth }}
        * - **Minimum Depth**
          - {{ min_depth }}
        * - **Average Depth**
          - {{ avg_depth }}
        * - **Depth Variance**
          - {{ depth_variance }}
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - {{ max_breadth }}
        * - **Minimum Breadth**
          - {{ min_breadth }}
        * - **Average Breadth**
          - {{ avg_breadth }}
        * - **Breadth Variance**
          - {{ breadth_variance }}
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - {{ num_term_types }}
        * - **Taxonomic Relations**
          - {{ num_taxonomic_relations }}
        * - **Non-taxonomic Relations**
          - {{ num_non_taxonomic_relations }}
        * - **Average Terms per Type**
          - {{ avg_terms_per_type }}
    ::

Usage Example
-------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import {{ class_name }}

    ontology = {{ class_name }}()
    ontology.load("path/to/{{ class_name }}-ontology.{{ format }}")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
""")

        context = {
            # Class metadata
            'ontology_name': ontology.ontology_full_name,
            'description': ontology.__doc__.replace("\n"," ").strip() if ontology.__doc__ else "No description available",
            'domain': ontology.domain,
            'category': ontology.category,
            'version': ontology.version,
            'last_updated': ontology.last_updated,
            'creator': ontology.creator,
            'license': ontology.license,
            'format': ontology.format.lower(),
            'download_url': ontology.download_url,
            'class_name': ontology.__class__.__name__,

            # Graph metrics
            'total_nodes': metrics.topology.total_nodes,
            'total_edges': metrics.topology.total_edges,
            'root_nodes': metrics.topology.num_root_nodes,
            'leaf_nodes': metrics.topology.num_leaf_nodes,

            # Knowledge coverage
            'num_classes': metrics.topology.num_classes,
            'num_individuals': metrics.topology.num_individuals,
            'num_properties': metrics.topology.num_properties,

            # Hierarchical metrics
            'max_depth': metrics.topology.max_depth,
            'min_depth': metrics.topology.min_depth,
            'avg_depth': f"{metrics.topology.avg_depth:.2f}",
            'depth_variance': f"{metrics.topology.depth_variance:.2f}",

            # Breadth metrics
            'max_breadth': metrics.topology.max_breadth,
            'min_breadth': metrics.topology.min_breadth,
            'avg_breadth': f"{metrics.topology.avg_breadth:.2f}",
            'breadth_variance': f"{metrics.topology.breadth_variance:.2f}",

            # Dataset statistics
            'num_term_types': metrics.dataset.num_term_types,
            'num_taxonomic_relations': metrics.dataset.num_taxonomic_relations,
            'num_non_taxonomic_relations': metrics.dataset.num_non_taxonomic_relations,
            'avg_terms_per_type': f"{metrics.dataset.avg_terms:.2f}"
        }

        content = documentation_template.render(context)
        return content

    @staticmethod
    def create_domain_readme(domain: str,
                             domain_definition: str,
                             metrics: dict[str, dict] = None) -> str:
        """
        Create README.md content for a domain repository on Hugging Face.

        This method generates a comprehensive README file for domain-specific
        ontology repositories, including metadata, ontology tables, usage examples,
        and citation information. The README follows Hugging Face dataset card
        conventions with proper YAML frontmatter.

        Args:
            domain: Domain identifier (e.g., "food_and_beverage").
            domain_definition: Descriptive text explaining the domain scope.
            metrics: Dictionary mapping ontology IDs to their metrics data.
                    Each entry should contain 'metrics', 'ontology_id',
                    'ontology_full_name', and 'domain' keys.

        Returns:
            Complete README.md content as a string, including:
            - YAML frontmatter with license, tags, and metadata
            - Domain overview and description
            - Table of ontologies with key statistics
            - Usage examples with OntoLearner
            - Citation information
        """
        domain_title = domain.replace('_', ' ').title()

        readme = f"""
---
license: mit
language:
- en
tags:
- OntoLearner
- Ontology-Learning
- {domain_title.replace(' ','-')}
- Benchmark-Ontologies
pretty_name: {domain_title}
---

<div align="center">
    <img  src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/main/images/logo.png"  alt="OntoLearner"
        style="display: block; margin: 0 auto; width: 500px; height: auto;">
    <h1 style="text-align: center; margin-top: 1em;">{domain_title} Domain Ontologies</h1>
    <a href="https://github.com/sciknoworg/OntoLearner"><img src="https://img.shields.io/badge/GitHub-OntoLearner-blue?logo=github" /></a>
</div>

## Overview
{domain_definition}

"""

        readme += """
| Ontology ID | Full Name | Classes | Properties | Last Updated |
|-------------|-----------|---------|------------|-------------|
"""
        usage_example_ontology = ""
        for metrics_data in metrics.values():
            metrics_data_domain = metrics_data.get("domain", "").lower().replace(' ', '_')
            if metrics_data_domain == domain:
                ontology_id = metrics_data["ontology_id"]
                ontology_full_name = metrics_data["ontology_full_name"]
                num_classes = metrics_data["metrics"].topology.num_classes
                num_properties = metrics_data["metrics"].topology.num_properties
                # num_individuals = metrics_data["metrics"].topology.num_individuals
                last_updated = metrics_data['last_updated']
                if usage_example_ontology == "":
                    usage_example_ontology = ontology_id

                readme += f"| {ontology_id} | {ontology_full_name} | {num_classes} | {num_properties} | {last_updated}|\n"

        readme += f"""
## Dataset Files
Each ontology directory contains the following files:
1. `<ontology_id>.<format>` - The original ontology file
2. `term_typings.json` - Dataset of term to type mappings
3. `taxonomies.json` - Dataset of taxonomic relations
4. `non_taxonomic_relations.json` - Dataset of non-taxonomic relations
5. `<ontology_id>.rst` - Documentation describing the ontology

## Usage
These datasets are intended for ontology learning research and applications. Here's how to use them with OntoLearner:

First of all, install the `OntoLearner` library via PiP:

```bash
pip install ontolearner
```

**How to load an ontology or LLM4OL Paradigm tasks datasets?**
``` python
from ontolearner import {usage_example_ontology}

ontology = {usage_example_ontology}()

# Load an ontology.
ontology.load()

# Load (or extract) LLMs4OL Paradigm tasks datasets
data = ontology.extract()
```

**How use the loaded dataset for LLM4OL Paradigm task settings?**
``` python
# Import core modules from the OntoLearner library
from ontolearner import {usage_example_ontology}, LearnerPipeline, train_test_split

# Load the {usage_example_ontology} ontology, which contains concepts related to wines, their properties, and categories
ontology = {usage_example_ontology}()
ontology.load()  # Load entities, types, and structured term annotations from the ontology
ontological_data = ontology.extract()

# Split instances into train and test sets
train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)

# Initialize a multi-component learning pipeline (retriever + LLM)
# This configuration enables a Retrieval-Augmented Generation (RAG) setup
pipeline = LearnerPipeline(
    retriever_id='sentence-transformers/all-MiniLM-L6-v2',      # Dense retriever model for nearest neighbor search
    llm_id='Qwen/Qwen2.5-0.5B-Instruct',                        # Lightweight instruction-tuned LLM for reasoning
    hf_token='...',                                             # Hugging Face token for accessing gated models
    batch_size=32,                                              # Batch size for training/prediction if supported
    top_k=5                                                     # Number of top retrievals to include in RAG prompting
)

# Run the pipeline: training, prediction, and evaluation in one call
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    evaluate=True,              # Compute metrics like precision, recall, and F1
    task='term-typing'          # Specifies the task
                                # Other options: "taxonomy-discovery" or "non-taxonomy-discovery"
)

# Print final evaluation metrics
print("Metrics:", outputs['metrics'])

# Print the total time taken for the full pipeline execution
print("Elapsed time:", outputs['elapsed_time'])

# Print all outputs (including predictions)
print(outputs)
```

For more detailed documentation, see the [![Documentation](https://img.shields.io/badge/Documentation-ontolearner.readthedocs.io-blue)](https://ontolearner.readthedocs.io)

""" + """## Citation

If you find our work helpful, feel free to give us a cite.

```bibtex
@inproceedings{babaei2023llms4ol,
  title={LLMs4OL: Large language models for ontology learning},
  author={Babaei Giglou, Hamed and D’Souza, Jennifer and Auer, S{\"o}ren},
  booktitle={International Semantic Web Conference},
  pages={408--427},
  year={2023},
  organization={Springer}
}
```
"""
        return readme

    def update_domain_readme(self,
                             repo_path: Path,
                             metrics_file_path: Path,
                             domain: str):
        """
        Update the README.md file in a domain repository.

        This method updates the README.md file for a domain repository by loading
        existing metrics and generating fresh content. It automatically discovers
        ontologies in the domain and includes their statistics in the README.

        Args:
            repo_path: Path to the local repository directory.
            metrics_file_path: Path to the Excel file containing ontology metrics.
            domain: Domain identifier for the repository.
            domain_definition: Optional custom domain definition. If None,
                             uses the default definition and attempts to improve
                             it using GPT-4o.

        Raises:
            FileNotFoundError: If the repository path doesn't exist.
            Exception: If README generation or file writing fails.

        Side Effects:
            - Creates or overwrites README.md in the repository root
            - May call OpenAI API to improve domain definitions
        """
        metrics = self.load_metrics_from_excel(metrics_file_path) if metrics_file_path.exists() else {}

        if len(metrics) == 0:
             raise FileNotFoundError(f"No metrics found in {metrics_file_path}")

        # Use default domain definition if not provided
        domain_definition = DOMAIN_DESCRIPTIONS[domain]

        # Create README content
        readme_content = self.create_domain_readme(
            domain=domain,
            domain_definition=domain_definition,
            metrics=metrics
        )
        # Write README.md file
        readme_path = repo_path / "README.md"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)

    @staticmethod
    def load_metrics_from_excel(metrics_file: Path) -> Dict[str, dict]:
        """
        Load metrics for all ontologies from the Excel file generated by processor.

        Args:
            metrics_file: Path to the Excel file containing metrics.

        Returns:
            Dictionary mapping ontology IDs to their metrics data.
            Each entry contains 'metrics', 'ontology_id', 'ontology_full_name',
            and 'domain' keys.
        """
        if not metrics_file.exists():
            logger.warning(f"Metrics file not found: {metrics_file}")
            return {}

        metrics = {}
        try:
            df = pd.read_excel(metrics_file)
            for _, row in df.iterrows():
                # Create topology metrics
                topology_metrics = TopologyMetrics(
                    total_nodes=row["total_nodes"],
                    total_edges=row["total_edges"],
                    num_classes=row["num_classes"],
                    num_properties=row["num_properties"],
                    num_individuals=row["num_individuals"],
                    max_depth=row["max_depth"],
                    min_depth=row["min_depth"],
                    avg_depth=row["avg_depth"],
                    depth_variance=row["depth_variance"],
                    max_breadth=row["max_breadth"],
                    min_breadth=row["min_breadth"],
                    avg_breadth=row["avg_breadth"],
                    breadth_variance=row["breadth_variance"],
                    num_root_nodes=row["num_root_nodes"],
                    num_leaf_nodes=row["num_leaf_nodes"],
                )

                # Create dataset metrics
                dataset_metrics = DatasetMetrics(
                    num_term_types=row["num_term_types"],
                    num_taxonomic_relations=row["num_taxonomic_relations"],
                    num_non_taxonomic_relations=row["num_non_taxonomic_relations"],
                    avg_terms=row["avg_terms"]
                )

                # Create ontology metrics
                ontology_metrics = OntologyMetrics(
                    name=row["Ontology Name"],
                    topology=topology_metrics,
                    dataset=dataset_metrics
                )

                # Store with additional metadata to match export format
                ontology_id = row["Ontology ID"]
                metrics[ontology_id] = {
                    "metrics": ontology_metrics,
                    "ontology_id": ontology_id,
                    "ontology_full_name": row["Ontology Full Name"],
                    "domain": row["Domain"],
                    "processing_time": row["Processing Time (s)"],
                    "last_updated": row["Last Updated"]
                }

            logger.info(f"Loaded metrics for {len(metrics)} ontologies from Excel file")
            return metrics
        except Exception as e:
            logger.error(f"Error loading metrics from Excel file: {e}")
            return {}

    def export_metrics_to_excel(self, metrics_file_path: Path = None) -> None:
        """
        Export all collected metrics to an Excel file with intelligent merging.

        This method exports ontology metrics to an Excel file, intelligently merging
        with existing data to preserve metrics from previous processing runs. It
        updates metrics for ontologies processed in the current session while
        preserving data for other ontologies.

        The Excel file contains comprehensive metrics including:
        - Ontology metadata (ID, name, domain)
        - Topology metrics (nodes, edges, depth, breadth)
        - Dataset statistics (term types, relations)
        - Processing performance data

        Args:
            metrics_file_path: Optional custom path for the Excel file.
                             If None, uses self.metrics_dir / "metrics.xlsx".

        Side Effects:
            - Creates or updates Excel file at specified path
            - Logs warnings if existing file cannot be read
        """

        if not metrics_file_path:
            raise ValueError(f"The {metrics_file_path} directory must exist!")
        excel_path = metrics_file_path

        # Try to read existing Excel file if it exists
        existing_df = None
        if excel_path.exists():
            try:
                existing_df = pd.read_excel(excel_path)
            except Exception as e:
                logger.warning(f"Could not read existing metrics file: {e}. Creating a new file.")
                pass

        # Create DataFrame from current metrics
        current_rows = []

        metrics: OntologyMetrics = self.processed_ontology['metrics']
        row = {
            "Ontology ID": self.processed_ontology["ontology_id"],
            "Ontology Full Name": self.processed_ontology["ontology_full_name"],
            "Domain": self.processed_ontology["domain"],
            "Ontology Name": metrics.name,
            "Processing Time (s)": self.processed_ontology["processing_time"],
            **metrics.topology.dict(),
            **metrics.dataset.dict(),
            "Last Updated": self.processed_ontology["last_updated"],
        }
        current_rows.append(row)
        current_df = pd.DataFrame(current_rows)

        # Merge existing and current metrics
        if existing_df is not None and not existing_df.empty:
            # Remove rows for ontologies that are in the current metrics (to be updated)
            current_ontology_ids = current_df["Ontology ID"].tolist()
            existing_df = existing_df[~existing_df["Ontology ID"].isin(current_ontology_ids)]

            # Concatenate existing (minus updated ones) with current
            final_df = pd.concat([existing_df, current_df], ignore_index=True)

            # Sort by Ontology ID for consistency
            final_df = final_df.sort_values("Ontology ID").reset_index(drop=True)
        else:
            final_df = current_df

        if not final_df.empty:
            # Sort the DataFrame by processing time (descending) to see which ontologies took longest
            final_df = final_df.sort_values("Processing Time (s)", ascending=False).reset_index(drop=True)

        # Write to Excel
        final_df.to_excel(excel_path, index=False)

    def push_to_hub(self, hf_token: str) -> Dict[str, Any]:
        """
        Push ontology and its extracted datasets to Hugging Face Hub.

        This method processes the ontology, extracts learning datasets, and uploads
        everything to the appropriate Hugging Face repositories. It handles both
        the domain-specific ontology repository and the global metrics repository.

        The method performs the following steps:
        1. Process the ontology and extract metrics using the Processor
        2. Clone or create the domain-specific Hugging Face repository
        3. Clone or create the global metrics repository
        4. Copy ontology files, datasets, and documentation
        5. Update metrics and domain README files
        6. Commit and push changes to both repositories

        Returns:
            Dictionary containing upload results with keys:
            - status: "success" if upload completed successfully
            - repository: Domain-specific repository ID
            - metrics_repository: Global metrics repository ID
            - ontology_id: The ontology identifier
            - url: URL to the domain repository
            - metrics_url: URL to the metrics repository

        Raises:
            ValueError: If required ontology attributes are missing.
            KeyError: If required environment variables are not set.
            Exception: If repository operations or file uploads fail.
        """
        api = HfApi()
        api.token = hf_token

        if self.processed_ontology is None:
            raise ValueError("The ontology is not processed!")

        if not all([self.processed_ontology['ontology_id'],
                    self.processed_ontology['domain'],
                    self.processed_ontology['format']]):
            raise ValueError("Ontology must have id, domain, and format defined")

        domain_normalized = self.processed_ontology['domain'].lower().replace(' ', '_')
        repo_id = f"SciKnowOrg/ontolearner-{domain_normalized}"
        metrics_repo_id = "SciKnowOrg/OntoLearner-Benchmark-Metrics"

        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)
            ontology_repo_path = tmp_path / "ontology_repo"
            metrics_repo_path = tmp_path / "metrics_repo"

            # Clone ontology repository
            try:
                api.repo_info(repo_id=repo_id, repo_type="dataset")
                repo = Repository(local_dir=ontology_repo_path, clone_from=repo_id, repo_type="dataset", token=hf_token)
                repo.git_pull()
            except RepositoryNotFoundError:
                api.create_repo(repo_id=repo_id, repo_type="dataset", private=False, token=hf_token)
                repo = Repository(local_dir=ontology_repo_path, clone_from=repo_id, repo_type="dataset", token=hf_token)

            # Clone metrics space repository
            try:
                api.repo_info(repo_id=metrics_repo_id, repo_type="space")
                metrics_repo = Repository(local_dir=metrics_repo_path, clone_from=metrics_repo_id, repo_type="space", token=hf_token)
                metrics_repo.git_pull()
            except RepositoryNotFoundError:
                # If metrics repo doesn't exist, create it (though it should exist)
                api.create_repo(repo_id=metrics_repo_id, repo_type="space", private=False, token=hf_token)
                metrics_repo = Repository(local_dir=metrics_repo_path, clone_from=metrics_repo_id, repo_type="space", token=hf_token)

            # Create ontology directory in the ontology repo
            self.save_resource(output_dir=str(ontology_repo_path), processed_ontology=self.processed_ontology)

            # Update metrics in the metrics repository
            metrics_file_path = metrics_repo_path / "metrics.xlsx"
            self.export_metrics_to_excel(metrics_file_path)

            # Update domain README.md in the ontology repository
            self.update_domain_readme(ontology_repo_path, metrics_file_path, domain_normalized)

            # Commit and push ontology repository
            repo.git_add(auto_lfs_track=True)
            commit_message = f":sparkles: Added {self.ontology_id} ontology!"
            repo.git_commit(commit_message)
            repo.git_push()

            # Commit and push metrics repository
            metrics_repo.git_add(auto_lfs_track=True)
            metrics_commit_message = f":memo: Update metrics for {self.ontology_id}"
            metrics_repo.git_commit(metrics_commit_message)
            metrics_repo.git_push()

            result = {
                "status": "success",
                "repository": repo_id,
                "metrics_repository": metrics_repo_id,
                "ontology_id": self.ontology_id,
                "url": f"https://huggingface.co/datasets/{repo_id}",
                "metrics_url": f"https://huggingface.co/spaces/{metrics_repo_id}"
            }

            return result
