from typing import Dict, Union
from typing import List
from uuid import uuid4
from pydantic import BaseModel, Field


class Term(BaseModel):
    """Schema for a term extracted from documents"""
    term: str = Field(..., min_length=1)
    extraction_method: str = Field("abstractive", description="extractive/abstractive")


class DocumentReference(BaseModel):
    """Reference to a document with extraction method"""
    doc_id: Union[int, str]
    extraction_method: str


class Document(BaseModel):
    """Schema for a document"""
    id: Union[int, str]
    title: str
    text: str


class TextualData(BaseModel):
    """Schema for textual data from a single split"""
    terms: List[Term] = []
    documents: List[Document] = []
    term2documents: Dict[str, List[DocumentReference]] = {}


class TermTyping(BaseModel):
    """
    Schema for term typing (Task A)
    """
    ID: str = Field(default_factory=lambda: f"TT_{str(uuid4())[:8]}", description="Unique identifier for the term")
    term: str = Field(..., description="The term being typed")
    types: List[str] = Field(..., description="List of types assigned to the term")


class TaxonomicRelation(BaseModel):
    """
    Schema for taxonomy relations (Task B)
    """
    ID: str = Field(default_factory=lambda: f"TR_{str(uuid4())[:8]}", description="Unique identifier for the relation")
    parent: str = Field(..., description="First term in taxonomy relation")
    child: str = Field(..., description="Second term in taxonomy relation")


class NonTaxonomicRelation(BaseModel):
    """
    Schema for non-taxonomic relations (Task C)
    """
    ID: str = Field(default_factory=lambda: f"NR_{str(uuid4())[:8]}", description="Unique identifier for the relation")
    head: str = Field(..., description="Head term in the relation")
    tail: str = Field(..., description="Tail term in the relation")
    relation: str = Field(..., description="Type of relation")


class TypeTaxonomies(BaseModel):
    """
    Schema for taxonomy information
    """
    types: List[str] = Field(..., description="List of types in the taxonomy")
    taxonomies: List[TaxonomicRelation] = Field(..., description="List of taxonomic relations")


class NonTaxonomicRelations(BaseModel):
    """
    Schema for non-taxonomic relation information
    """
    types: List[str] = Field(..., description="List of types involved in relations")
    relations: List[str] = Field(..., description="List of relation types")
    non_taxonomies: List[NonTaxonomicRelation] = Field(..., description="List of non-taxonomic relations")


class OntologyData(BaseModel):
    """
    Schema for complete ontology data
    """
    term_typings: List[TermTyping] = Field(..., description="List of term typing entries")
    type_taxonomies: TypeTaxonomies = Field(..., description="Taxonomy information")
    type_non_taxonomic_relations: NonTaxonomicRelations = Field(..., description="Non-taxonomic relation information")

class PseudoSentence(BaseModel):
    id: str
    pseudo_sentences: List[str]
    terms: List[str]
    types: List[str]


class SyntheticText2OntoData(BaseModel):
    """
    Schema for synthetic text2onto generator
    """
    child_to_parent: Dict[str, List[str]] = Field(..., description="Mapping from child terms to their parent terms")
    pseudo_sentences: List[PseudoSentence] = Field(..., description="List of pseudo sentence batches with metadata")
    generated_docs: List[Document] = Field(..., description="Generated documents from pseudo sentences")
