from ..base import AutoPrompt


class StandardizedPrompting(AutoPrompt):
    def __init__(self, prompt_template: str = None, task: str = None):
        if prompt_template is None:
            if task == "A":
                prompt_template = """
Given a list of types as candidates to be assigned to the term, identify the most probable types.

Term: {term}
Candidates: {context}

Return types only in the form of a Python list. Do not provide any explanation.
"""
            elif task == "B":
                prompt_template = """
Is {parent} a parent of {child}?
Answer yes/no. Do not explain.
"""
            elif task == "C":
                prompt_template = """
What is the relation between {head} and {tail}? Return only the relation type.
"""
        super().__init__(prompt_template)

    def format(self, **kwargs):
        return self.prompt_template.format(**kwargs)
