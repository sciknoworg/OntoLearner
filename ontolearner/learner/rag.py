import re
from typing import Any, List

from ..base import AutoLearner
from ..data_structure import OntologyData


class AutoRAGLearner(AutoLearner):
    def __init__(self, learner_retriever: Any, learner_llm: Any, prompting: Any):
        super().__init__()
        self.retriever = learner_retriever
        self.llm = learner_llm
        self.prompting = prompting

    def load(self, retriever_id: str, llm_id: str):
        self.retriever.load(retriever_id)
        self.llm.load(llm_id)

    @staticmethod
    def _prepare_documents(data: OntologyData, task: str) -> List[str]:
        documents = []
        if task == "term-typing":
            for tt in data.term_typings:
                documents.append(f"Term: {tt.term}\nTypes: {', '.join(tt.types)}")
        elif task == "taxonomy-discovery":
            for tr in data.type_taxonomies.taxonomies:
                documents.append(f"Parent: {tr.parent}\nChild: {tr.child}\nRelation: is-a")
        elif task == "task-non-taxonomic-relations":
            for nr in data.type_non_taxonomic_relations.non_taxonomies:
                documents.append(f"Head: {nr.head}\nRelation: {nr.relation}\nTail: {nr.tail}")
        return documents

    def fit(self, train_data: OntologyData, task: str):
        documents = self._prepare_documents(train_data, task)
        self.retriever.index(documents)
        return self

    def predict(self, eval_data: Any, task: str) -> List[str]:
        if task == "term-typing":
            term = eval_data
            query = term
            prompt_data = {"term": term}
        elif task == "taxonomy-discovery":
            parent, child = eval_data
            query = f"{parent} {child}"
            prompt_data = {"parent": parent, "child": child}
        elif task == "task-non-taxonomic-relations":
            head, tail = eval_data
            query = f"{head} {tail}"
            prompt_data = {"head": head, "tail": tail}
        else:
            raise ValueError(f"Task {task} not supported")

        context = "\n".join(self.retriever.retrieve(query, top_k=5))

        prompting = self.prompting.format(term=prompt_data["term"], context=context)

        raw_response = self.llm.generate([prompting])[0]

        if task == "term-typing":
            match = re.search(r'\[(.*?)\]', raw_response)
            if match:
                types_str = match.group(1)
                types = [t.strip().strip("'\"") for t in types_str.split(',')]
                return types
            return [raw_response.strip()]

        return [raw_response]
