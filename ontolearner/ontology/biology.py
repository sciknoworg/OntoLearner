
from ..base import BaseOntology


class LIFO(BaseOntology):
    """
    The Life Ontology (LifO) is an ontology of the life of organism. LifO represents the
    life processes of organisms and related entities and relations. LifO is a general
    purpose ontology that covers the common features associated with different
    organisms such as unicellular prokaryotes (e.g., E. coli) and multicellular organisms (e.g., human).

    This class processes Life Ontology using default behavior.
    """
    ontology_full_name = "Life Ontology (LifO)"


class GO(BaseOntology):
    """
    The Gene Ontology (GO) Provides structured controlled vocabularies for the annotation of gene products
    with respect to their molecular function, cellular component, and biological role.

    This class processes Gene Ontology using default behavior.
    """
    ontology_full_name = "Gene Ontology (GO)"


class MarineTLO(BaseOntology):
    """
    MarineTLO is a top level ontology, generic enough to provide consistent abstractions or
    specifications of concepts included in all data models or ontologies of marine data sources and
    provide the necessary properties to make this distributed knowledge base a coherent source of
    facts relating observational data with the respective spatiotemporal context and categorical
    (systematic) domain knowledge. It can be used as the core schema for publishing Linked Data, as
    well as for setting up integration systems for the marine domain. It can be extended to any level
    of detail on demand, while preserving monotonicity. For its development and evolution we have
    adopted an iterative and incremental methodology where a new version is released every two
    months. For the implementation we use OWL 2, and to evaluate it we use a set of competency
    queries, formulating the domain requirements provided by the related communities.

    This class processes MarineTLO Ontology using default behavior.
    """
    ontology_full_name = "Marine Taxonomy and Life Ontology (MarineTLO)"


class BioPAX(BaseOntology):
    """
    BioPAX is a standard language that aims to enable integration, exchange, visualization and analysis
    of biological pathway data. Specifically, BioPAX supports data exchange between pathway data
    groups and thus reduces the complexity of interchange between data formats by providing an
    accepted standard format for pathway data.

    This class processes BioPAX Ontology using default behavior.
    """
    ontology_full_name = "Biological Pathways Exchange (BioPAX)"


class EFO(BaseOntology):
    """
    The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables
    available in EBI databases, and for projects such as the GWAS catalog. It combines parts of several biological ontologies,
    such as UBERON anatomy, ChEBI chemical compounds, and Cell Ontology. The scope of EFO is to support the annotation,
    analysis and visualization of data handled by many groups at the EBI and as the core ontology for Open Targets.
    EFO is developed by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT).

    This class processes Experimental Factor Ontology using default behavior.
    """
    ontology_full_name = "Experimental Factor Ontology (EFO)"


class PATO(BaseOntology):
    """
    An ontology of phenotypic qualities (properties, attributes or characteristics).

    This class processes Phenotype and Trait Ontology (PATO) using default behavior.
    """
    ontology_full_name = "Phenotype and Trait Ontology (PATO)"


class PO(BaseOntology):
    """
    The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
    morphology and growth and development to plant genomics data.

    This class processes Plant Ontology using default behavior.
    """
    ontology_full_name = "Plant Ontology (PO)"


class Microscopy(BaseOntology):
    """
    The Microscopy Ontology (MO) extends the ontological framework of the PMDco. The MO facilitates semantic integration
    and the interoperable connection of diverse data sources from the fields of microscopy and microanalysis. Consequently,
    the MO paves the way for new, adaptable data applications and analyses across various experiments and studies

    This class processes Microscopy Ontology using default behavior.
    """
    ontology_full_name = "Microscopy Ontology (MO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True
