from ..base.textual import BaseTextualDataset


class OLLMWikipedia(BaseTextualDataset):
    """
    OLLM Wikipedia is a synthetic ontology generated from Wikipedia articles.
    It is used to evaluate the performance of ontology learning algorithms.
    The ontology is generated from the Wikipedia dump and contains concepts and their relationships.

    This class processes OLLM Wikipedia using default textual processing methods.
    """
    ontology_full_name: str = "OLLM Wikipedia Ontology"
