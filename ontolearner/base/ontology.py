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

import logging
import os
import re
import json
from pathlib import Path
from abc import ABC
import concurrent.futures
from typing import List, Tuple, Any, Set, Optional


from rdflib import Graph, OWL, URIRef, RDFS, RDF
import pandas as pd
import networkx as nx
from huggingface_hub import hf_hub_download

from ..data_structure import (OntologyData, TermTyping, TaxonomicRelation, NonTaxonomicRelation,
                              TypeTaxonomies, NonTaxonomicRelations, OntologyMetrics)

logger = logging.getLogger(__name__)


class BaseOntology(ABC):
    """
    Abstract base class for ontology processing and data extraction.

    This class provides a standardized interface for loading, processing, and extracting
    structured data from ontologies across different domains. It supports both local
    file loading and automatic downloading from Hugging Face repositories.
    """
    ontology_id: str = None
    ontology_full_name: str = None
    domain: str = None
    category: str = None
    version: str = None
    last_updated: str = None
    creator: str = None
    license: str = None
    format: str = None
    download_url = None
    loaded_from_huggingface = False
    loaded_from_local = False

    def __init__(self, language: str = 'en', base_dir: Optional[str] = None) -> None:
        """
        Initialize the ontology instance.

        Args:
            language: Language code for label extraction (default: 'en').
                     Used when multiple language labels are available.
            base_dir: Base directory for resolving relative import paths.
                     Useful when ontology imports other local files.
        """
        self.rdf_graph: Optional[Graph] = None
        self.nx_graph: Optional[nx.DiGraph] = None
        self.language = language
        self.base_dir = base_dir

    def __str__(self):
        return (
            f"ontology_id: {self.ontology_id}\n"
            f"ontology_full_name: {self.ontology_full_name}\n"
            f"domain: {self.domain}\n"
            f"category: {self.category}\n"
            f"version: {self.version}\n"
            f"last_updated: {self.last_updated}\n"
            f"creator: {self.creator}\n"
            f"license: {self.license}\n"
            f"format: {self.format}\n"
            f"download_url: {self.download_url}\n"
        )

    def from_huggingface(self):
        """
        Download an ontology file from a Hugging Face repository.

        This method constructs the appropriate repository ID and filename based on
        the OntoLearner naming conventions and downloads the ontology file to a
        local cache directory.

        Args:
            ontology_id: Unique identifier for the ontology (e.g., "wine").
            domain: Domain category (e.g., "Food & Beverage").
            format: File format extension (e.g., "owl", "rdf").

        Returns:
            Local file path to the downloaded ontology file.

        Raises:
            ValueError: If any required parameter is missing or empty.
            Exception: If download fails due to network issues, authentication,
                      or file not found in repository.
        """
        ontology_domain = self.domain.lower().replace(' ', '_')
        repo_id = f"SciKnowOrg/ontolearner-{ontology_domain}"
        filename = f"{self.ontology_id.lower()}/{self.ontology_id.lower()}.{self.format.lower()}"
        try:
            file_path = hf_hub_download(repo_id=repo_id, filename=filename, repo_type="dataset")
            self.rdf_graph = Graph()
            self._load(file_path)
        except Exception:
            raise

    def from_local(self, path: str):
        """
        Validate and return a local ontology file path.

        This method checks if the specified local file exists and returns the
        path if valid. It serves as a validation step for local file loading.

        Args:
            path: File system path to the local ontology file.

        Returns:
            The same path if the file exists and is accessible.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Ontology file not found at {path}")
        self.rdf_graph = Graph()
        self._load(path)

    def load(self, path: Optional[str] = None) -> None:
        """
        Load an ontology from a local file or Hugging Face repository.

        This method is the main entry point for loading ontologies. It automatically
        determines the source (local vs. Hugging Face) based on whether a path is
        provided, handles RDF parsing, and processes any owl:imports statements.

        Args:
            path: Optional local file path. If provided, loads from local file.
                 If None, downloads from Hugging Face using class attributes
                 (ontology_id, domain, format).

        Raises:
            ValueError: If the loaded ontology contains no RDF triples.
            FileNotFoundError: If local file path is invalid.
            Exception: If download from Hugging Face fails or RDF parsing fails.
        """
        self.loaded_from_huggingface = False
        self.loaded_from_local = False
        try:
            if path:
                # Use provided path as local file
                self.from_local(path)
                self.loaded_from_local = True
            else:
                # Download from HuggingFace
                self.from_huggingface()
                self.loaded_from_huggingface = True
            if len(self.rdf_graph) == 0:
                raise ValueError("Loaded ontology contains no triples")
        except Exception:
            raise

    def _load(self, path: str, visited: Optional[set] = None) -> None:
        if visited is None:
            visited = set()
        if path in visited:
            return
        visited.add(path)

        self.rdf_graph.parse(path)

        if not self.contains_imports():
            return

        # Process owl:imports
        for ontology in self.rdf_graph.subjects(RDF.type, OWL.Ontology):
            for import_def in self.rdf_graph.objects(ontology, OWL.imports):
                import_uri = self._resolve_import_def(import_def)

                if import_uri:
                    try:
                        self._load(import_uri, visited)
                    except Exception as e:
                        logger.error(f"Failed to load import {import_uri}: {str(e)}")
                        pass
                else:
                    logger.warning(f"Could not resolve import: {import_def}")
                    pass


    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return False

    def _resolve_import_def(self, uri: URIRef) -> Optional[str]:
        """Resolve imported URIs to local file paths."""
        uri_str = str(uri)

        # Handle OBO PURLs
        if uri_str.startswith("http://purl.obolibrary.org/obo/"):
            path = uri_str.replace("http://purl.obolibrary.org/obo/", "")
            if self.base_dir:
                local_path = os.path.join(self.base_dir, path)
                if os.path.exists(local_path):
                    return local_path
            # Fallback to HTTP if local file not found
            return uri_str
        # Handle other HTTP URIs
        elif uri_str.startswith("http://") or uri_str.startswith("https://"):
            return uri_str
        # Handle file:// URIs
        elif uri_str.startswith("file:///"):
            file_path = uri_str[8:]
        elif uri_str.startswith("file://"):
            file_path = uri_str[7:]
        else:
            file_path = uri_str

        # Convert path separators to Unix style
        file_path = file_path.replace('\\', '/')

        # Handle Windows drive letter
        if ':' in file_path and os.name == 'nt':
            file_path = file_path.split(':', 1)[1]

        if self.base_dir:
            resolved_path = os.path.join(self.base_dir, file_path.lstrip('/'))
            if os.path.exists(resolved_path):
                return resolved_path

        return None

    def extract(self, reinforce_extraction: bool = False) -> OntologyData:
        """
        Extract structured learning data from the loaded ontology.

        This method extracts three types of ontological information needed for
        machine learning tasks: term typings, taxonomic relations, and non-taxonomic
        relations. The extraction strategy depends on the data source.

        For local ontologies, it performs live extraction from the RDF graph.
        For Hugging Face ontologies, it downloads pre-processed JSON files for
        efficiency, with an option to force live extraction.

        Args:
            reinforce_extraction: If True and loaded from Hugging Face, forces
                                 live extraction from RDF instead of using
                                 pre-processed JSON files. Useful for debugging
                                 or when pre-processed data is outdated.

        Returns:
            OntologyData object containing:
            - term_typings: List of term-to-type mappings
            - type_taxonomies: Hierarchical relationships between types
            - type_non_taxonomic_relations: Non-hierarchical relationships

        Raises:
            ValueError: If ontology has not been loaded yet.
            Exception: If extraction fails due to malformed data or network issues.
        """
        if not (self.loaded_from_local or self.loaded_from_huggingface):
            raise ValueError("Ontology must be loaded before extraction")

        if self.loaded_from_local:
            return self._extract_from_local()
        else:
            return self._extract_from_huggingface(reinforce_extraction)

    def _extract_from_local(self) -> OntologyData:
        """Extract data from local ontology source."""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            term_typings_future = executor.submit(self.extract_term_typings)
            taxonomies_future = executor.submit(self.extract_type_taxonomies)
            non_taxonomic_future = executor.submit(self.extract_type_non_taxonomic_relations)

            term_typings = term_typings_future.result()
            types, taxonomies = taxonomies_future.result()
            types_nt, relations, non_taxonomies = non_taxonomic_future.result()

            return OntologyData(
                term_typings=term_typings,
                type_taxonomies=TypeTaxonomies(
                    types=types,
                    taxonomies=taxonomies
                ),
                type_non_taxonomic_relations=NonTaxonomicRelations(
                    types=types_nt,
                    relations=relations,
                    non_taxonomies=non_taxonomies
                )
            )

    def _extract_from_huggingface(self, reinforce_extraction: bool=False) -> Optional[OntologyData]:
        """Extract data from HuggingFace, with optional reinforcement."""
        ontology_domain = self.domain.lower().replace(' ', '_')
        repo_id = f"SciKnowOrg/ontolearner-{ontology_domain}"
        ontology_id = self.ontology_id.lower()
        original_huggingface = self.loaded_from_huggingface
        original_local = self.loaded_from_local

        if reinforce_extraction:
            try:
                self.loaded_from_huggingface = False
                self.loaded_from_local = True
                result = self.extract(reinforce_extraction=False)
                return result
            except Exception:
                pass
            finally:
                self.loaded_from_huggingface = original_huggingface
                self.loaded_from_local = original_local
        try:
            term_typings_path = hf_hub_download(repo_id=repo_id,
                                                filename=f"{ontology_id}/term_typings.json",
                                                repo_type="dataset")
            taxonomies_path = hf_hub_download(repo_id=repo_id,
                                              filename=f"{ontology_id}/type_taxonomies.json",
                                              repo_type="dataset")
            non_taxonomic_path = hf_hub_download(repo_id=repo_id,
                                                 filename=f"{ontology_id}/type_non_taxonomic_relations.json",
                                                 repo_type="dataset")

            with open(term_typings_path, 'r') as f:
                term_typings = json.load(f)
            with open(taxonomies_path, 'r') as f:
                type_taxonomies = json.load(f)
            with open(non_taxonomic_path, 'r') as f:
                type_non_taxonomic_relations = json.load(f)

            return OntologyData(
                term_typings=term_typings,
                type_taxonomies=type_taxonomies,
                type_non_taxonomic_relations=type_non_taxonomic_relations
            )
        except Exception as e:
            raise ValueError(f"Failed to extract ontology data from HuggingFace: {str(e)}") from e

    def _update_metrics_space(self, metrics_file_path: Path, metrics: OntologyMetrics) -> None:
        """Update the metrics file in the OntoLearner metrics space."""

        # Load existing metrics or create new DataFrame
        if metrics_file_path.exists():
            df = pd.read_excel(metrics_file_path)
        else:
            df = pd.DataFrame()

        new_row = {
            "Ontology ID": self.ontology_id,
            "Ontology Full Name": self.ontology_full_name,
            "Domain": self.domain,
            "Ontology Name": metrics.name,
            "Processing Time (s)": 0,  # TODO: Add processing time
            **metrics.topology.dict(),
            **metrics.dataset.dict()
        }

        # Update or append row
        if len(df) > 0 and self.ontology_id in df["Ontology ID"].values:
            df.loc[df["Ontology ID"] == self.ontology_id] = pd.Series(new_row)
        else:
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # Save updated metrics
        df.to_excel(metrics_file_path, index=False)

    @staticmethod
    def is_valid_label(label: str) -> Any:
        invalids = ['root', 'thing']
        if label.lower() in invalids:
            return None
        return label

    def get_label(self, uri: str) -> str:
        """
        Extracts the label for a given URI in the specified language from the RDF graph.
        If no valid label is found, returns None.
        """
        entity = URIRef(uri)
        labels = list(self.rdf_graph.objects(subject=entity, predicate=RDFS.label))
        for label in labels:
            if hasattr(label, 'language') and label.language == self.language:
                return self.is_valid_label(str(label))
        if labels:
            first_label = str(labels[0])
            if len(first_label) > 3 and not first_label.startswith("http"):
                return self.is_valid_label(first_label)
        if "#" in uri:
            local_name = uri.split("#")[-1]
        elif "/" in uri:
            local_name = uri.split("/")[-1]
        else:
            local_name = uri
        label = self.is_valid_label(local_name)
        return label

    def build_graph(self) -> None:
        """
        Build NetworkX graph from RDF data.

        This method should be implemented by each specific ontology class
        to handle their unique graph structure.
        """
        self.nx_graph = nx.DiGraph()

        if not self.rdf_graph:
            ontology_domain = self.domain.lower().replace(' ', '_')
            repo_id = f"SciKnowOrg/ontolearner-{ontology_domain}"
            ontology_id = self.ontology_id.lower()
            file_path = hf_hub_download(
                repo_id=repo_id,
                filename=f"{ontology_id}/{ontology_id}.{self.format.lower()}",
                repo_type="dataset"
            )

            self.load(file_path)

        for subject, predicate, obj in self.rdf_graph:
            subject_label = self.get_label(str(subject))
            object_label = self.get_label(str(obj))
            predicate_label = self.get_label(str(predicate))
            if subject_label and object_label and predicate_label:
                self.nx_graph.add_node(subject_label)
                self.nx_graph.add_node(object_label)
                self.nx_graph.add_edge(subject_label, object_label, label=predicate_label)

    # ------------------- Term Typings -------------------
    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term-to-type mappings (e.g., instances of classes).
        """
        term_typings = []
        for class_uri in self._get_relevant_classes():
            for instance in self._get_instances_for_class(class_uri):
                term = self.get_label(uri=str(instance))
                types = self.get_label(uri=str(class_uri))
                # Filter out anonymous class identifiers
                if (term and types and
                        not self._is_anonymous_id(term) and
                        not self._is_anonymous_id(types)):
                    term_typings.append(TermTyping(term=term, types=[types]))
        return term_typings

    def _get_relevant_classes(self) -> Set[URIRef]:
        """Hook: Define which classes to process (default: all classes)."""
        return (set(self.rdf_graph.subjects(RDF.type, RDFS.Class)) |
                set(self.rdf_graph.subjects(RDF.type, OWL.Class)))

    def _get_instances_for_class(self, class_uri: URIRef) -> Set[URIRef]:
        """Hook: Get instances of a class (default: direct instances)."""
        return set(self.rdf_graph.subjects(RDF.type, class_uri))

    # ------------------- Taxonomy Extraction -------------------
    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """
        Extract taxonomy from the ontology
        """
        types, taxonomies = [], []
        subclasses = self.rdf_graph.subjects(predicate=RDFS.subClassOf)
        for subclass in subclasses:
            parent_classes = self.rdf_graph.objects(subject=subclass, predicate=RDFS.subClassOf)
            subclass_label = self.get_label(str(subclass))
            for parent in parent_classes:
                parent_label = self.get_label(uri=str(parent))
                if (subclass_label and parent_label and
                        not self._is_anonymous_id(subclass_label) and
                        not self._is_anonymous_id(parent_label)):
                    types.append(subclass_label)
                    types.append(parent_label)
                    taxonomies.append(TaxonomicRelation(parent=parent_label, child=subclass_label))
        types = list(set(types))
        return types, taxonomies

    # ------------------- Non-Taxonomic Relations -------------------
    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from the ontology.
        """
        types_set = set()
        relations_set = set()
        non_taxonomic_pairs: List[NonTaxonomicRelation] = []

        for s, p, o in self.rdf_graph:
            if self._is_valid_non_taxonomic_triple(s, p, o):
                head = self.get_label(str(s))
                tail = self.get_label(str(o))
                relation = self.get_label(str(p))

                # Filter out anonymous class identifiers
                if (head and tail and relation and
                        not self._is_anonymous_id(head) and
                        not self._is_anonymous_id(tail)):
                    non_taxonomic_pairs.append(
                        NonTaxonomicRelation(head=head, tail=tail, relation=relation)
                    )
                    types_set.update([head, tail])
                    relations_set.add(relation)

        types = sorted(types_set)
        relations = sorted(relations_set)
        return types, relations, non_taxonomic_pairs

    def _is_valid_non_taxonomic_triple(self, s: URIRef, p: URIRef, o: URIRef) -> bool:
        """Validate non-taxonomic relations between named classes (URIRefs only)."""
        return (
            self.check_if_class(s) and
            self.check_if_class(o) and
            p != RDFS.subClassOf
        )

    def check_if_class(self, entity):
        """Check if an entity is a class (i.e., rdf:type rdfs:Class or owl:Class)."""
        for _, _, obj in self.rdf_graph.triples((entity, RDF.type, None)):
            if obj in (RDFS.Class, OWL.Class):
                return True
        return False

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Check if a label represents an anonymous class identifier."""
        if not label:
            return True

        # Common RDF/OWL blank node patterns
        if label.startswith('_:'):  # Standard RDF blank node notation
            return True
        if label.startswith('genid-'):  # Common OWL tools like Protégé
            return True
        if label.startswith('nodeID://'):  # Some RDF serializers
            return True

        # Numeric patterns
        if re.match(r'^N[0-9]+$', label):
            return True
        if re.match(r'^_[0-9]+$', label):
            return True
        if re.match(r'^c_[0-9]+$', label):
            return True
        if re.match(r'^BFO_[0-9]+$', label):
            return True
        if re.match(r'^IAO_[0-9]+$', label):
            return True
        if re.match(r'^OBI_[0-9]+$', label):
            return True
        if re.match(r'^FIX_[0-9]+$', label):
            return True
        if re.match(r'^REX_[0-9]+$', label):
            return True
        if re.match(r'^UO_[0-9]+$', label):
            return True
        if re.match(r'^MS_[0-9]+$', label):
            return True
        if re.match(r'^AFRL_[0-9]+$', label):
            return True
        if re.match(r'^AFFN_[0-9]+$', label):
            return True
        if re.match(r'^AFE_[0-9]+$', label):
            return True
        if re.match(r'^AFQ_[0-9]+$', label):
            return True
        if re.match(r'^AFP_[0-9]+$', label):
            return True
        if re.match(r'^AFM_[0-9]+$', label):
            return True
        if re.match(r'^AFC_[0-9]+$', label):
            return True
        if re.match(r'^ENVO_[0-9]+$', label):
            return True
        if re.match(r'^AFR_[0-9]+$', label):
            return True

        # Hexadecimal patterns
        if re.match(r'^N[0-9a-f]{32}$', label, re.IGNORECASE):
            return True
        if re.match(r'^n[0-9a-f]+$', label, re.IGNORECASE):
            return True
        if re.match(r'^b[0-9a-f]+$', label, re.IGNORECASE):
            return True
        if re.match(r'^c_[0-9a-f]+$', label, re.IGNORECASE):
            return True

        # UUID patterns
        if re.match(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', label, re.IGNORECASE):
            return True

        # Auto-generated node patterns
        if re.match(r'^node_[0-9a-f_]+$', label, re.IGNORECASE):
            return True
        if re.match(r'^auto_gen_[0-9a-zA-Z]+$', label):
            return True
        if re.match(r'^blank[0-9]+$', label):
            return True

        # Tool-specific patterns
        if label.startswith('ARQ'):  # Apache Jena ARQ
            return True
        if label.startswith('jena-'):  # Apache Jena
            return True
        if label.startswith('bnode'):  # Some RDF tools
            return True

        # Image and label patterns
        if re.match(r'^img_', label):  # Any string starting with img_
            return True
        if re.match(r'^xl_', label):   # Any string starting with xl_
            return True
        if re.match(r'^xl-', label):   # Any string starting with xl-
            return True

        # SKOS Collection patterns
        if re.match(r'^skosCollection_[0-9a-f]+$', label):
            return True

        if re.match(r'^PMD_[0-9]+$', label):
            return True

        return False
