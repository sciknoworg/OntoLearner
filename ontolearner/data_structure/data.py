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

from typing import Dict, Union
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class Term(BaseModel):
    """
    Schema for a term extracted from textual documents.

    Represents a single term (word or phrase) that has been identified and
    extracted from text using either extractive or abstractive methods.
    Used in text-to-ontology workflows for term identification.

    Attributes:
        term: The extracted term text (minimum 1 character).
        extraction_method: Method used for extraction, either "extractive"
                          (directly from text) or "abstractive" (generated/inferred).
    """
    term: str = Field(..., min_length=1)
    extraction_method: str = Field("abstractive", description="extractive/abstractive")


class DocumentReference(BaseModel):
    """
    Reference linking a term to a document with extraction metadata.

    Represents the relationship between a term and the document it was
    extracted from, including information about the extraction method used.
    Enables traceability of terms back to their source documents.

    Attributes:
        doc_id: Unique identifier for the source document.
        extraction_method: Method used to extract the term from this document.
    """
    doc_id: Union[int, str]
    extraction_method: str


class Document(BaseModel):
    """
    Schema for a textual document in the corpus.

    Represents a single document containing text from which terms and
    ontological knowledge can be extracted. Forms the basis for
    text-to-ontology learning workflows.

    Attributes:
        id: Unique identifier for the document.
        title: Document title or heading.
        text: Full text content of the document.
    """
    id: Union[int, str]
    title: str
    text: str


class TextualData(BaseModel):
    """
    Schema for textual data from a single processing split.

    Aggregates all textual information for a specific data split, including
    extracted terms, source documents, and the mapping between them.
    Used in text-to-ontology pipelines to organize and track relationships
    between terms and their source documents.

    Attributes:
        terms: List of terms extracted from the documents.
        documents: List of source documents in this split.
        term2documents: Mapping from term strings to lists of document
                       references showing which documents contain each term.
    """
    terms: List[Term] = []
    documents: List[Document] = []
    term2documents: Dict[str, List[DocumentReference]] = {}


class TermTyping(BaseModel):
    """
    Schema for term typing data (Ontology Learning Task 1).

    Represents the assignment of semantic types to terms, which is the first
    fundamental task in ontology learning. Each instance captures a term and
    its associated types, enabling machine learning models to learn patterns
    for predicting types of new terms.

    This corresponds to the question: "What type(s) does this term belong to?"
    For example: "Chardonnay" → ["WhiteWine", "Wine", "AlcoholicBeverage"]

    Attributes:
        ID: Unique identifier with "TT_" prefix (auto-generated).
        term: The term being classified (e.g., "Chardonnay", "Einstein").
        types: List of semantic types assigned to the term. Can be multiple
               types due to multiple inheritance in ontologies.
    """
    ID: str = Field(default_factory=lambda: f"TT_{str(uuid4())[:8]}", description="Unique identifier for the term")
    term: str = Field(..., description="The term being typed")
    types: List[str] = Field(..., description="List of types assigned to the term")


class TaxonomicRelation(BaseModel):
    """
    Schema for taxonomic relations (Ontology Learning Task 2).

    Represents hierarchical "is-a" relationships between concepts, which form
    the taxonomic backbone of ontologies. Each instance captures a parent-child
    relationship that defines the ontological hierarchy.

    This corresponds to the question: "Is concept A a parent of concept B?"
    For example: "Wine" is-a-parent-of "RedWine" → True

    Attributes:
        ID: Unique identifier with "TR_" prefix (auto-generated).
        parent: The more general concept in the hierarchy.
        child: The more specific concept that is a subclass of parent.
    """
    ID: str = Field(default_factory=lambda: f"TR_{str(uuid4())[:8]}", description="Unique identifier for the relation")
    parent: str = Field(..., description="First term in taxonomy relation")
    child: str = Field(..., description="Second term in taxonomy relation")


class NonTaxonomicRelation(BaseModel):
    """
    Schema for non-taxonomic relations (Ontology Learning Task 3).

    Represents non-hierarchical relationships between concepts, capturing
    semantic associations beyond simple "is-a" relationships. These relations
    express how concepts interact, relate, or depend on each other.

    This corresponds to the question: "What is the relationship between A and B?"
    For example: "Wine" madeFrom "Grape", "Person" livesIn "City"

    Attributes:
        ID: Unique identifier with "NR_" prefix (auto-generated).
        head: The subject/source entity in the relationship.
        tail: The object/target entity in the relationship.
        relation: The type of relationship connecting head and tail.
    """
    ID: str = Field(default_factory=lambda: f"NR_{str(uuid4())[:8]}", description="Unique identifier for the relation")
    head: str = Field(..., description="Head term in the relation")
    tail: str = Field(..., description="Tail term in the relation")
    relation: str = Field(..., description="Type of relation")


class TypeTaxonomies(BaseModel):
    """
    Aggregated schema for taxonomic information in an ontology.

    Collects all taxonomic relationships and the types involved in them,
    providing a complete view of the hierarchical structure of an ontology.
    Used to organize and access all "is-a" relationships for learning tasks.

    Attributes:
        types: Complete list of all types/concepts that participate in
               taxonomic relationships (both as parents and children).
        taxonomies: List of all taxonomic relations in the ontology,
                   defining the hierarchical structure.
    """
    types: List[str] = Field(..., description="List of types in the taxonomy")
    taxonomies: List[TaxonomicRelation] = Field(..., description="List of taxonomic relations")


class NonTaxonomicRelations(BaseModel):
    """
    Aggregated schema for non-taxonomic relation information in an ontology.

    Collects all non-hierarchical relationships, the types involved, and the
    relation types used, providing a complete view of the non-taxonomic
    semantic structure of an ontology.

    Attributes:
        types: List of all types/concepts that participate in non-taxonomic
               relationships (as either head or tail entities).
        relations: List of all unique relation types used in the ontology
                  (e.g., "madeFrom", "locatedIn", "hasColor").
        non_taxonomies: List of all non-taxonomic relation instances,
                       defining the semantic associations between concepts.
    """
    types: List[str] = Field(..., description="List of types involved in relations")
    relations: List[str] = Field(..., description="List of relation types")
    non_taxonomies: List[NonTaxonomicRelation] = Field(..., description="List of non-taxonomic relations")


class OntologyData(BaseModel):
    """
    Complete schema for all ontology learning data extracted from an ontology.

    This is the main data container that aggregates all three types of
    ontological information needed for machine learning tasks. It represents
    the complete structured knowledge extracted from an ontology file.

    The three components correspond to the three fundamental ontology learning tasks:
    1. Term typing: What types do terms belong to?
    2. Taxonomy discovery: What are the hierarchical relationships?
    3. Non-taxonomic relation discovery: What are the semantic associations?

    Attributes:
        term_typings: All term-to-type mappings for learning type prediction.
        type_taxonomies: All hierarchical relationships and involved types.
        type_non_taxonomic_relations: All semantic associations and relation types.
    """
    term_typings: List[TermTyping] = Field(..., description="List of term typing entries")
    type_taxonomies: TypeTaxonomies = Field(..., description="Taxonomy information")
    type_non_taxonomic_relations: NonTaxonomicRelations = Field(..., description="Non-taxonomic relation information")


class PseudoSentence(BaseModel):
    """
    Schema for pseudo-sentence generation with associated metadata.

    Represents a batch of artificially generated sentences along with the
    terms and types they contain. Used in synthetic text-to-ontology
    generation workflows to create training data.

    Attributes:
        id: Unique identifier for this pseudo-sentence batch.
        pseudo_sentences: List of generated sentence texts.
        terms: List of terms that appear in these sentences.
        types: List of types associated with the terms.
    """
    id: str
    pseudo_sentences: List[str]
    terms: List[str]
    types: List[str]


class SyntheticText2OntoData(BaseModel):
    """
    Schema for synthetic text-to-ontology generation data.

    Aggregates all data produced by synthetic text generation workflows,
    including hierarchical mappings, pseudo-sentences, and generated documents.
    Used to create artificial training corpora for text-to-ontology learning.

    This schema supports workflows that generate synthetic text from existing
    ontological structures to augment training data or create controlled
    experimental conditions.

    Attributes:
        child_to_parent: Hierarchical mapping showing parent-child relationships
                        between terms, derived from ontological taxonomies.
        pseudo_sentences: List of generated pseudo-sentence batches with
                         associated terms and types.
        generated_docs: Complete documents generated from pseudo-sentences,
                       ready for use in text-to-ontology pipelines.
    """
    child_to_parent: Dict[str, List[str]] = Field(..., description="Mapping from child terms to their parent terms")
    pseudo_sentences: List[PseudoSentence] = Field(..., description="List of pseudo sentence batches with metadata")
    generated_docs: List[Document] = Field(..., description="Generated documents from pseudo sentences")
