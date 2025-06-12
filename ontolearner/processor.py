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
import os
from pathlib import Path
from typing import Union, Dict, List
from jinja2 import Template
import time
import pandas as pd

from .base import BaseOntology
from .data_structure import OntologyMetrics, OntologyData, DatasetMetrics, TopologyMetrics
from .tools import Analyzer
from .utils import io

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


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

SYSTEM_PROMPT = """
As an ontology domain expert, enhance this domain definition with precision and academic clarity.

Domain: {domain}
Current definition: {domain_definition}

The OntoLearner library includes these ontologies in this domain (for context only):
{ontologies}

Create a concise, enhanced domain definition (2-3 sentences) that:
- Accurately describes the domain's scope and technical focus
- Highlights its significance in knowledge representation
- Avoids any reference to specific ontologies in the definition

Enhanced definition:
"""


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

    def __init__(self, datasets_dir: Path, templates_dir: Path, benchmark_dir: Path,  metrics_dir: Path, analyzer_class: type[Analyzer] = Analyzer):
        """
        Initialize the Processor with directory paths and configuration.

        Args:
            datasets_dir (Path): Directory to save extracted datasets
            templates_dir (Path): Directory containing documentation templates
            benchmark_dir (Path): Directory to save generated documentation
            metrics_dir (Path): Directory to save metrics files
            analyzer_class (type, optional): Class to use for ontology analysis. Defaults to Analyzer.
        """
        self.datasets_dir = datasets_dir
        self.templates_dir = templates_dir
        self.benchmark_dir = benchmark_dir
        self.metrics_dir = metrics_dir
        self.analyzer_class = analyzer_class
        self.all_metrics: Dict[str, dict] = {}
        self.doc_template_path = templates_dir / "ontology.rst"
        self.doc_template = Template(self.doc_template_path.read_text())

    def process_ontology(self, ontology: BaseOntology, ontology_path: Union[str, Path]) \
            -> OntologyMetrics:
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

        try:
            if not Path(ontology_path).exists():
                raise ValueError(f"Ontology file not found: {ontology_path}")

            ontology.load(str(ontology_path))
            # ontology.load()

            data: OntologyData = ontology.extract()
            ontology.build_graph()
            analyzer = self.analyzer_class()
            metrics: OntologyMetrics = analyzer(ontology)

            end_time = time.time()
            processing_time = end_time - start_time

            self.all_metrics[ontology.ontology_id] = {
                "metrics": metrics,
                "ontology_id": ontology.ontology_id,
                "ontology_full_name": ontology.ontology_full_name,
                "domain": ontology.domain,
                "processing_time": processing_time
            }
            self.save_datasets(data, ontology)
            self.build_documentation(ontology, metrics)
            return metrics
        except Exception:
            raise

    def save_datasets(self, data: OntologyData, ontology: BaseOntology) -> None:
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
        for dataset_type in ['term_typings', 'type_taxonomies', 'type_non_taxonomic_relations']:
            domain_dir = self.datasets_dir / f"{ontology.domain.lower().replace(' ', '_')}"
            domain_dir.mkdir(parents=True, exist_ok=True)

            save_path = domain_dir / f"{ontology.ontology_id.lower().replace(' ', '_')}/{dataset_type}.json"
            io.save_json(data.model_dump()[dataset_type], save_path)

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
        context = {
            # Class metadata
            'ontology_name': ontology.ontology_full_name,
            'description': ontology.__doc__.strip() if ontology.__doc__ else "No description available",
            'domain': ontology.domain,
            'category': ontology.category,
            'version': ontology.version,
            'last_updated': ontology.last_updated,
            'creator': ontology.creator,
            'license': ontology.license,
            'format': ontology.format,
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

        content = self.doc_template.render(context)
        domain_dir = self.benchmark_dir / f"{ontology.domain.lower().replace(' ', '_')}"
        domain_dir.mkdir(parents=True, exist_ok=True)
        doc_path = domain_dir / f"{ontology.ontology_id.lower()}.rst"

        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(content)

        return doc_path



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
- ontology-learning
- {domain}
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
| Ontology ID | Full Name | Classes | Properties | Individuals |
|-------------|-----------|---------|------------|-------------|
"""
        for metrics_data in metrics.values():
            metrics_data_domain = metrics_data.get("domain", "").lower().replace(' ', '_')

            if metrics_data_domain == domain:
                ontology_id = metrics_data["ontology_id"]
                ontology_full_name = metrics_data["ontology_full_name"]
                num_classes = metrics_data["metrics"].topology.num_classes
                num_properties = metrics_data["metrics"].topology.num_properties
                num_individuals = metrics_data["metrics"].topology.num_individuals

                readme += f"| {ontology_id} | {ontology_full_name} | {num_classes} | {num_properties} | {num_individuals}|\n"

        readme += """
## Dataset Files
Each ontology directory contains the following files:
1. `<ontology_id>.<format>` - The original ontology file
2. `term_typings.json` - Dataset of term to type mappings
3. `taxonomies.json` - Dataset of taxonomic relations
4. `non_taxonomic_relations.json` - Dataset of non-taxonomic relations
5. `<ontology_id>.rst` - Documentation describing the ontology

## Usage
These datasets are intended for ontology learning research and applications. Here's how to use them with OntoLearner:

```python
from ontolearner import LearnerPipeline, AutoLearnerLLM, Wine, train_test_split

# Load ontology (automatically downloads from Hugging Face)
ontology = Wine()
ontology.load()

# Extract the dataset
data = ontology.extract()

# Split into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Create a learning pipeline (for RAG-based learning)
pipeline = LearnerPipeline(
    task="term-typing",  # Other options: "taxonomy-discovery" or "non-taxonomy-discovery"
    retriever_id="sentence-transformers/all-MiniLM-L6-v2",
    llm_id="mistralai/Mistral-7B-Instruct-v0.1",
    hf_token="your_huggingface_token"  # Only needed for gated models
)

# Train and evaluate
results, metrics = pipeline.fit_predict_evaluate(
    train_data=train_data,
    test_data=test_data,
    top_k=3,
    test_limit=10
)
```

For more detailed examples, see the [OntoLearner documentation](https://ontolearner.readthedocs.io/).

## Citation
If you use these ontologies in your research, please cite:

```bibtex
@software{babaei_giglou_2025,
  author       = {Babaei Giglou, Hamed and D'Souza, Jennifer and Aioanei, Andrei and Mihindukulasooriya, Nandana and Auer, Sören},
  title        = {OntoLearner: A Modular Python Library for Ontology Learning with LLMs},
  month        = may,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.15399783},
  url          = {https://doi.org/10.5281/zenodo.15399783},
}
```
"""

        return readme

    def update_domain_readme(self,
                             repo_path: Path,
                             metrics_file_path: Path,
                             domain: str,
                             domain_definition: str = None) -> None:
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

        # Use default domain definition if not provided
        if domain_definition is None:
            domain_definition = self.improve_domain_definition(
                domain,
                DOMAIN_DEFINITIONS[domain],
                []
            )

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
                    total_nodes=row.get("total_nodes", 0),
                    total_edges=row.get("total_edges", 0),
                    num_classes=row.get("num_classes", 0),
                    num_properties=row.get("num_properties", 0),
                    num_individuals=row.get("num_individuals", 0),
                    max_depth=row.get("max_depth", 0),
                    min_depth=row.get("min_depth", 0),
                    avg_depth=row.get("avg_depth", 0),
                    depth_variance=row.get("depth_variance", 0),
                    max_breadth=row.get("max_breadth", 0),
                    min_breadth=row.get("min_breadth", 0),
                    avg_breadth=row.get("avg_breadth", 0),
                    breadth_variance=row.get("breadth_variance", 0),
                    num_root_nodes=row.get("num_root_nodes", 0),
                    num_leaf_nodes=row.get("num_leaf_nodes", 0)
                )

                # Create dataset metrics
                dataset_metrics = DatasetMetrics(
                    num_term_types=row.get("num_term_types", 0),
                    num_taxonomic_relations=row.get("num_taxonomic_relations", 0),
                    num_non_taxonomic_relations=row.get("num_non_taxonomic_relations", 0),
                    avg_terms=row.get("avg_terms", 0)
                )

                # Create ontology metrics
                ontology_metrics = OntologyMetrics(
                    name=row.get("Ontology Name", ""),
                    topology=topology_metrics,
                    dataset=dataset_metrics
                )

                # Store with additional metadata to match export format
                ontology_id = row.get("Ontology ID", "")
                metrics[ontology_id] = {
                    "metrics": ontology_metrics,
                    "ontology_id": ontology_id,
                    "ontology_full_name": row.get("Ontology Full Name", ""),
                    "domain": row.get("Domain", ""),
                    "processing_time": row.get("Processing Time (s)", 0)
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
        if not self.all_metrics:
            return

        excel_path = metrics_file_path if metrics_file_path else self.metrics_dir / "metrics.xlsx"

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
        for ontology_id, data in self.all_metrics.items():
            metrics: OntologyMetrics = data["metrics"]
            row = {
                "Ontology ID": data["ontology_id"],
                "Ontology Full Name": data["ontology_full_name"],
                "Domain": data["domain"],
                "Ontology Name": metrics.name,
                "Processing Time (s)": data["processing_time"],
                **metrics.topology.dict(),
                **metrics.dataset.dict()
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

    @staticmethod
    def improve_domain_definition(domain: str,
                                  domain_definition: str,
                                  ontologies: List[BaseOntology]) -> str:
        """
        Improve domain definition using GPT-4o for enhanced clarity and precision.

        This method leverages OpenAI's GPT-4o model to enhance domain definitions
        with academic precision and technical clarity. It provides context about
        the ontologies in the domain while ensuring the definition remains general
        and doesn't reference specific ontologies.

        Args:
            domain: Domain identifier (e.g., "food_and_beverage").
            domain_definition: Current definition text to be improved.
            ontologies: List of ontology instances in the domain for context.
                       Used to inform the improvement but not referenced directly
                       in the output definition.

        Returns:
            Enhanced domain definition (2-3 sentences) with improved:
            - Technical accuracy and precision
            - Academic clarity and professionalism
            - Scope description and significance
            - Knowledge representation focus
        """
        try:
            gpt_4o_llm = ChatOpenAI(
                api_key = os.environ['OPENAI_API_KEY'],
                model = "gpt-4o",
                temperature = 0,
            )
            prompt = PromptTemplate(input_variables=["domain", "domain_definition", "ontologies"], template=SYSTEM_PROMPT)
            chain = prompt | gpt_4o_llm | StrOutputParser()

            result = chain.invoke(
                {
                    "domain": domain,
                    "domain_definition": domain_definition,
                    "ontologies": "\n".join([f"- {ontology.ontology_full_name}" for ontology in ontologies])
                }
            )
            return result
        except Exception as e:
            logger.error(f"Failed to improve domain definition: {str(e)}", exc_info=True)
            return domain_definition
