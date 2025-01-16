
from typing import List, Optional
from pydantic import BaseModel, Field


class TermTyping(BaseModel):
    """
    Schema for term typing (Task A)
    """
    term: str = Field(..., description="The term being typed")
    types: List[str] = Field(..., description="List of types assigned to the term")


class TaxonomyRelation(BaseModel):
    """
    Schema for taxonomy relations (Task B)
    """
    term1: str = Field(..., description="First term in taxonomy relation")
    term2: str = Field(..., description="Second term in taxonomy relation")
    relation: bool = Field(..., description="Whether a taxonomic relation exists")
    relationship_type: Optional[str] = Field(None, description="Type of relationship (e.g., 'direct')")


class NonTaxonomicRelation(BaseModel):
    """
    Schema for non-taxonomic relations (Task C)
    """
    head: str = Field(..., description="Head term in the relation")
    tail: str = Field(..., description="Tail term in the relation")
    relation: str = Field(..., description="Type of relation")
    valid: Optional[bool] = Field(None, description="Whether the relation is valid")


class OntologyData(BaseModel):
    """
    Schema for complete ontology data
    """
    term_typings: List[TermTyping]
    type_taxonomies: dict = Field(..., description="Dictionary containing types and taxonomies")
    type_non_taxonomic_relations: dict = Field(..., description="Dictionary containing non-taxonomic relations")
