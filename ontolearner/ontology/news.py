from ..base.ontology import BaseOntology


class BBC(BaseOntology):
    """
    The BBC ontology codifies the logic that connects web documents, BBC products and platforms
    for which content is available. Currently, there are 10 major products in Future Media
    which produce content for BBC online. The majority of those contain more products dedicated in thematic areas,
    for example Education propositions are part of the K&L (Knowledge and Learning) product portfolio.
    """
    ontology_id = "BBC"
    ontology_full_name = "BBC Ontology"


class BBCBusiness(BaseOntology):
    """
    The Business News Ontology describes the concepts that occur in BBC business news.
    """
    ontology_id = "BBCBusiness"
    ontology_full_name = "BBC Business News Ontology"


class BBCCMS(BaseOntology):
    """
    The Content Management Systems ontology defines the terms that LDP needs to interact with systems that produce content.
    The linked data platform contain semantic metadata for the creative content and also the things the BBC produces content about.
    The CMS ontology defines how these things and content are associated with other BBC instances of the same thing.
    """
    ontology_id = "BBCCMS"
    ontology_full_name = "BBC CMS Ontology"


class BBCCoreConcepts(BaseOntology):
    """
    The generic BBC ontology for people, places, events, organisations, themes which represent things
    that make sense across the BBC. This model is meant to be generic enough, and allow clients (domain experts)
    link their own concepts e.g., athletes or politicians using rdfs:sublClassOf the particular concept.
    ontology_id = "BBCCoreConcepts"
    """
    ontology_full_name = "BBC Core Concepts Ontology"


class BBCCreativeWork(BaseOntology):
    """
    This ontology defines the terms required to describe the creative works produced by the BBC and their associated metadata.
    This ontology powers reading and writing creative works in the triplestore using tags associated with them (about)
    their more specific types (BlogPost, NewsItem, Programme) and audiences (audience).
    """
    ontology_id = "BBCCreativeWork"
    ontology_full_name = "BBC Creative Work Ontology"


class BBCStoryline(BaseOntology):
    """
    The News Storyline Ontology is a generic model for describing and organising the stories news organisations tell.
    The ontology is intended to be flexible to support any given news or media publisher's approach to handling news stories.
    At the heart of the ontology, is the concept of Storyline. As a nuance of the English language the word 'story'
    has multiple meanings. In news organisations, a story can be an individual piece of content,
    such as an article or news report. It can also be the editorial view on events occurring in the world.
    """
    ontology_id = "BBCStoryline"
    ontology_full_name = "BBC Storyline Ontology"


class BBCFood(BaseOntology):
    """
    The Food Ontology is a simple lightweight ontology for publishing data about recipes,
    including the foods they are made from and the foods they create as well as the diets,
    menus, seasons, courses and occasions they may be suitable for. Whilst it originates in a specific BBC use case,
    the Food Ontology should be applicable to a wide range of recipe data publishing across the web.
    """
    ontology_id = "BBCFood"
    ontology_full_name = "BBC Food Ontology"


class BBCPolitics(BaseOntology):
    """
    The Politics Ontology describes the concepts that occur in BBC politics news.
    """
    ontology_id = "BBCPolitics"
    ontology_full_name = "BBC Politics News Ontology"


class BBCProgrammes(BaseOntology):
    """
    This ontology aims at providing a simple vocabulary for describing programmes.
    It covers brands, series (seasons), episodes, broadcast events, broadcast services,etc.
    Its development was funded by the BBC, and is heavily grounded on previous programmes data modelling work done there.
    """
    ontology_id = "BBCProgrammes"
    ontology_full_name = "BBC Programmes Ontology"


class BBCProvenance(BaseOntology):
    """
    An ontology to capture data about the provenance of data in an RDF Triple Store.
    This provenance is focused on the immediate providers and not the ultimate source,
    so for example, this would record that geodata was provided by the BBC Locator team,
    and not geonames. In the Linked Data Platform, this data is applied to contexts or named graphs.
    A named graph is, in effect, a 'fourth part' to a triple, hence the term 'quad store'.
    """
    ontology_id = "BBCProvenance"
    ontology_full_name = "BBC Provenance News Ontology"


class BBCSport(BaseOntology):
    """
    The Sport Ontology is a simple lightweight ontology for publishing data about competitive sports events.
    The terms in this ontology allow data to be published about:
    The structure of sports tournaments as a series of eventsThe competing of agents in a competitionThe type
    of discipline a event involvesThe award associated with the competition and how received it...etc
    Whilst it originates in a specific BBC use case, the Sport Ontology should be applicable
    to a wide range of competitive sporting events data publishing use cases.
    Care has been taken to try and ensure interoperability with more general ontologies in use.
    In particular, it draws heavily upon the events ontology.
    """
    ontology_id = "BBCSport"
    ontology_full_name = "BBC Sport Ontology"


class BBCWildlife(BaseOntology):
    """
    A simple vocabulary for describing biological species and related taxa. The vocabulary defines terms
    for describing the names and ranking of taxa, as well as providing support for describing their habitats,
    conservation status, and behavioural characteristics, etc.
    """
    ontology_id = "BBCWildlife"
    ontology_full_name = "BBC Wildlife Ontology"
