from ..base.ontology import BaseOntology


class CopyrightOnto(BaseOntology):
    """
    The Copyright Ontology tries to formalise the copyright domain as a way to facilitate
    automated (or computer-supported) copyright management through the whole content value chain,
    as it is shaped by copyright law. Therefore, it does not focus just on the last step,
    end-users permissions to consume content, like many rights languages and ontologies do.
    """
    ontology_id = "CopyrightOnto"
    ontology_full_name = "Copyright Ontology (CopyrightOnto)"
    domain = "Law"
    category = "Legal Knowledge"
    version = None
    last_updated = "2019-09"
    creator = "Rhizomik"
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://rhizomik.net/ontologies/copyrightonto/"
