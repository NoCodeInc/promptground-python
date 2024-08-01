class PromptRunResult:
    def __init__(self, content, usage):
        self.content = content
        self.usage = usage

    def __str__(self):
        return f'PromptRunResult(content="{self.content}", usage={self.usage})'