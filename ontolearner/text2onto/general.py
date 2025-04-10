from ..base.text2onto import BaseText2OntoDataset


class OLLMWikipedia(BaseText2OntoDataset):
    """
    OLLM Wikipedia is a synthetic ontology generated from Wikipedia articles.
    It is used to evaluate the performance of ontology learning algorithms.
    The ontology is generated from the Wikipedia dump and contains concepts and their relationships.

    This class processes OLLM Wikipedia using default textual processing methods.
    """
    dataset_id: str = "OLLMWikipedia"
    dataset_full_name: str = "OLLM Wikipedia Ontology"
