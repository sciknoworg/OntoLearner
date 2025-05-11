from ..base import AutoPrompt

class StandardizedPrompting(AutoPrompt):
    def __init__(self, prompt_template: str=None):
        if prompt_template is None:
            prompt_template = """ """
        super().__init__(prompt_template)

    def format(self, **kwargs):
        pass
