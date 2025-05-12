from ..base import AutoPrompt


class StandardizedPrompting(AutoPrompt):
    def __init__(self, prompt_template: str = None, task: str = None):
        if prompt_template is None:
            if task == "term-typing":
                prompt_template = """
Given a list of types as candidates to be assigned to the term, identify the most probable types.
Return the types only in the form of a list. Do not provide any explanation outside the list.

Term:
{term}

Candidates Types:
{context}

Response:
"""
            elif task == "taxonomy-discovery":
                prompt_template = """
Is {parent} a parent of {child}?
Answer yes/no. Do not explain.
"""
            elif task == "task-non-taxonomic-relations":
                prompt_template = """
What is the relation between {head} and {tail}? Return only the relation type.
"""

        super().__init__(prompt_template)

    def format(self, **kwargs):
        return self.prompt_template.format(**kwargs)
