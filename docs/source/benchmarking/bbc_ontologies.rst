BBC Ontologies
================

Overview
-----------------
This site provides access to the ontologies the BBC is using to support its audience
facing applications such as BBC Sport, BBC Education, BBC Music, News projects and more.
These ontologies form the basis of our Linked Data Platform.


BBC Ontology
================
The BBC ontology codifies the logic that connects web documents, BBC products and platforms
for which content is available. Currently, there are 10 major products in Future Media
which produce content for BBC online. The majority of those contain more products dedicated in thematic areas,
for example Education propositions are part of the K&L (Knowledge and Learning) product portfolio.

:Domain: Media
:Category: News
:Current Version: 1.37
:Last Updated: 	2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Homepage <https://www.bbc.co.uk/ontologies/bbc-ontology/>`_
:Documentation: `BBC Documentation <https://www.bbc.co.uk/ontologies/bbc-ontology/>`_

Base Metrics
---------------
    - Classes: 10
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 164
    - **Root Nodes**: 0
    - **Leaf Nodes**: 101
    - **Maximum Depth**: 0
    - **Edges**: 316

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 10
    - **Taxonomic Relations**: 35
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.91

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBC
   # Initialize and load ontology
   bbc = BBC()
   bbc.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Business News Ontology
=======================
The Business News Ontology describes the concepts that occur in BBC business news.

:Domain: Media
:Category: News
:Current Version: 0.5
:Last Updated: 	2014-11-09
:Producer: https://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, https://uk.linkedin.com/in/amaalmohamed
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Business Homepage <https://www.bbc.co.uk/ontologies/business-news-ontology>`_
:Documentation: `BBC Business Documentation <https://www.bbc.co.uk/ontologies/business-news-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 50
    - **Root Nodes**: 0
    - **Leaf Nodes**: 35
    - **Maximum Depth**: 0
    - **Edges**: 95

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCBusiness
   # Initialize and load ontology
   bbc_business = BBCBusiness()
   bbc_business.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_business.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


CMS Ontology
============
The Content Management Systems ontology defines the terms that LDP needs to interact with systems that produce content.
The linked data platform contain semantic metadata for the creative content and also the things the BBC produces content about.
The CMS ontology defines how these things and content are associated with other BBC instances of the same thing.

:Domain: Media
:Category: News
:Current Version: 3.7
:Last Updated: 	2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC CMS Homepage <https://www.bbc.co.uk/ontologies/cms-ontology>`_
:Documentation: `BBC CMS Documentation <https://www.bbc.co.uk/ontologies/cms-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 68
    - **Root Nodes**: 0
    - **Leaf Nodes**: 41
    - **Maximum Depth**: 0
    - **Edges**: 137

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 4
    - **Taxonomic Relations**: 17
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.67

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBC_CMS
   # Initialize and load ontology
   bbc_cms = BBC_CMS()
   bbc_cms.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_cms.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Core Concepts Ontology
=======================
The generic BBC ontology for people, places, events, organisations, themes which represent things
that make sense across the BBC. This model is meant to be generic enough, and allow clients (domain experts)
link their own concepts e.g., athletes or politicians using rdfs:sublClassOf the particular concept.

:Domain: Media
:Category: News
:Current Version: 1.30
:Last Updated: 2019-11-21
:Producer: jeremy.tarling@bbc.co.uk, tom.hodgkinson@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Core Concepts Homepage <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_
:Documentation: `BBC Core Concepts Documentation <https://www.bbc.co.uk/ontologies/core-concepts-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 122
    - **Root Nodes**: 4
    - **Leaf Nodes**: 73
    - **Maximum Depth**: 2
    - **Edges**: 265

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCCoreConcepts
   # Initialize and load ontology
   bbc_core_concepts = BBCCoreConcepts()
   bbc_core_concepts.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_core_concepts.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Creative Work Ontology
=======================
This ontology defines the terms required to describe the creative works produced by the BBC and their associated metadata.
This ontology powers reading and writing creative works in the triplestore using tags associated with them (about)
their more specific types (BlogPost, NewsItem, Programme) and audiences (audience).

:Domain: Media
:Category: News
:Current Version: 1.19
:Last Updated: 2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Creative Work Homepage <https://www.bbc.co.uk/ontologies/creative-work-ontology>`_
:Documentation: `BBC Creative Work Documentation <https://www.bbc.co.uk/ontologies/creative-work-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 137
    - **Root Nodes**: 0
    - **Leaf Nodes**: 80
    - **Maximum Depth**: 0
    - **Edges**: 300

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 15
    - **Taxonomic Relations**: 17
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.79

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCCreativeWork
   # Initialize and load ontology
   bbc_creative_work = BBCCreativeWork()
   bbc_creative_work.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_creative_work.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Storyline Ontology
==================
The News Storyline Ontology is a generic model for describing and organising the stories news organisations tell.
The ontology is intended to be flexible to support any given news or media publisher's approach to handling news stories.
At the heart of the ontology, is the concept of Storyline. As a nuance of the English language the word 'story'
has multiple meanings. In news organisations, a story can be an individual piece of content,
such as an article or news report. It can also be the editorial view on events occurring in the world.

:Domain: Media
:Category: News
:Current Version: 0.3
:Last Updated: 2013-05-01
:Producer: http://uk.linkedin.com/in/paulwilton, http://www.bbc.co.uk/blogs/internet/authors/Jeremy_Tarling, http://uk.linkedin.com/in/jarredmcginnis
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Curriculum Homepage <https://iptc.org/thirdparty/bbc-ontologies/storyline.html>`_
:Documentation: `BBC Curriculum Documentation <https://iptc.org/thirdparty/bbc-ontologies/storyline.html>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 74
    - **Root Nodes**: 0
    - **Leaf Nodes**: 53
    - **Maximum Depth**: 0
    - **Edges**: 157

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 2
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCStoryline
   # Initialize and load ontology
   bbc_storyline = BBCStoryline()
   bbc_storyline.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_storyline.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Food Ontology
=============
The Food Ontology is a simple lightweight ontology for publishing data about recipes,
including the foods they are made from and the foods they create as well as the diets,
menus, seasons, courses and occasions they may be suitable for. Whilst it originates in a specific BBC use case,
the Food Ontology should be applicable to a wide range of recipe data publishing across the web.

:Domain: Food
:Category: Food
:Current Version: 0.1
:Last Updated: 2014/03/18
:Producer:
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Food Homepage <https://www.bbc.co.uk/ontologies/food-ontology>`_
:Documentation: `BBC Food Documentation <https://www.bbc.co.uk/ontologies/food-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 108
    - **Root Nodes**: 0
    - **Leaf Nodes**: 63
    - **Maximum Depth**: 0
    - **Edges**: 267

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCFood
   # Initialize and load ontology
   bbc_food = BBCFood()
   bbc_food.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_food.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Politics Ontology
=================
An ontology which describes a model for politics, specifically in terms of local government and elections.

:Domain: Politics
:Category: News
:Current Version: 0.9
:Last Updated: 2014-01-06
:Producer: https://www.r4isstatic.com/
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Politics Homepage <https://www.bbc.co.uk/ontologies/politics-ontology>`_
:Documentation: `BBC Politics Documentation <https://www.bbc.co.uk/ontologies/politics-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 50
    - **Root Nodes**: 0
    - **Leaf Nodes**: 35
    - **Maximum Depth**: 0
    - **Edges**: 95

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 5
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCPolitics
   # Initialize and load ontology
   bbc_politics = BBCPolitics()
   bbc_politics.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_politics.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Programmes Ontology
===================
This ontology aims at providing a simple vocabulary for describing programmes.
It covers brands, series (seasons), episodes, broadcast events, broadcast services,etc.
Its development was funded by the BBC, and is heavily grounded on previous programmes data modelling work done there.

:Domain: Media
:Category: News
:Current Version: 1.1
:Last Updated: 2009/02/20
:Producer: https://moustaki.org/foaf.rdf#moustaki
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Programmes Homepage <https://www.bbc.co.uk/ontologies/programmes-ontology>`_
:Documentation: `BBC Programmes Documentation <https://www.bbc.co.uk/ontologies/programmes-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 218
    - **Root Nodes**: 2
    - **Leaf Nodes**: 129
    - **Maximum Depth**: 3
    - **Edges**: 620

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 40
    - **Non-taxonomic Relations**: 19
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCProgrammes
   # Initialize and load ontology
   bbc_programmes = BBCProgrammes()
   bbc_programmes.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_programmes.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Provenance Ontology
===================
An ontology to capture data about the provenance of data in an RDF Triple Store.
This provenance is focused on the immediate providers and not the ultimate source,
so for example, this would record that geodata was provided by the BBC Locator team,
and not geonames. In the Linked Data Platform, this data is applied to contexts or named graphs.
A named graph is, in effect, a 'fourth part' to a triple, hence the term 'quad store'.

:Domain: Media
:Category: News
:Current Version: 1.9
:Last Updated: 2012-12-01
:Producer: LinkedData@bbc.co.uk
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Provenance Homepage <https://www.bbc.co.uk/ontologies/provenance-ontology>`_
:Documentation: `BBC Provenance Documentation <https://www.bbc.co.uk/ontologies/provenance-ontology>`_

Base Metrics
---------------
    - Classes: 0
    - Individuals: 0
    - Properties: 0

Graph Metrics:
------------------
    - **Total Nodes**: 74
    - **Root Nodes**: 0
    - **Leaf Nodes**: 48
    - **Maximum Depth**: 0
    - **Edges**: 151

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 1
    - **Taxonomic Relations**: 6
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0.14

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCProvenance
   # Initialize and load ontology
   bbc_provenance = BBCProvenance()
   bbc_provenance.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_provenance.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Sport Ontology
==============
The Sport Ontology is a simple lightweight ontology for publishing data about competitive sports events.
The terms in this ontology allow data to be published about:
The structure of sports tournaments as a series of eventsThe competing of agents in a competitionThe type
of discipline a event involvesThe award associated with the competition and how received it...etc
Whilst it originates in a specific BBC use case, the Sport Ontology should be applicable
to a wide range of competitive sporting events data publishing use cases.
Care has been taken to try and ensure interoperability with more general ontologies in use.
In particular it draws heavily upon the events ontology.

:Domain: Sport
:Category: Sport
:Current Version: 3.2
:Last Updated:
:Producer: https://uk.linkedin.com/pub/jem-rayfield/27/b19/757, https://uk.linkedin.com/in/paulwilton, https://www.blockslabpillar.com, https://www.linkedin.com/in/tfgrahame, https://uk.linkedin.com/pub/stuart-williams/8/684/351, https://uk.linkedin.com/in/brianwmcbride
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Sport Homepage <https://www.bbc.co.uk/ontologies/sport-ontology>`_
:Documentation: `BBC Sport Documentation <https://www.bbc.co.uk/ontologies/sport-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 232
    - **Root Nodes**: 42
    - **Leaf Nodes**: 115
    - **Maximum Depth**: 3
    - **Edges**: 490

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 40
    - **Taxonomic Relations**: 25
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 2.35

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCSport
   # Initialize and load ontology
   bbc_sport = BBCSport()
   bbc_sport.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_sport.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations


Wildlife Ontology
=================
A simple vocabulary for describing biological species and related taxa. The vocabulary defines terms
for describing the names and ranking of taxa, as well as providing support for describing their habitats,
conservation status, and behavioural characteristics, etc.

:Domain: Biology
:Category: Biology
:Current Version: 	1.1
:Last Updated: 2013/12/18
:Producer: https://www.ldodds.com#me, http://tomscott.name/
:License: Creative Commons 4.0
:Format: TTL
:Download: `BBC Wildlife Homepage <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_
:Documentation: `BBC Wildlife Documentation <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_

Base Metrics
---------------
    - Classes:
    - Individuals:
    - Properties:

Graph Metrics:
------------------
    - **Total Nodes**: 157
    - **Root Nodes**: 1
    - **Leaf Nodes**: 93
    - **Maximum Depth**: 1
    - **Edges**: 414

Dataset Statistics
-----------------
Generated Benchmarks:
    - **Term Types**: 0
    - **Taxonomic Relations**: 23
    - **Non-taxonomic Relations**: 0
    - **Average Terms per Type**: 0

Usage Example
------------------
.. code-block:: python

   from ontolearner.ontology import BBCWildlife
   # Initialize and load ontology
   bbc_wildlife = BBCWildlife()
   bbc_wildlife.load("path/to/ontology.owl")
   # Extract datasets
   data = bbc_wildlife.extract()
   # Access specific relations
   term_types = data.term_typings
   taxonomic_relations = data.type_taxonomies
   non_taxonomic_relations = data.type_relations
   non_taxonomic_relations = data.type_non_taxonomic_relations
