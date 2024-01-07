class Agent:
    def __init__(self, editor_id: str, prompt: str, thread=None):
        self.editor_id = editor_id
        self.prompt = prompt
        self.thread = thread
