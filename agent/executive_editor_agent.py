import os
from dotenv import load_dotenv

from agent.agent import Agent


class ExecutiveEditor(Agent):
    def __init__(self, prompt, thread=None):
        load_dotenv()
        editor_id = os.getenv("EXECUTIVE_EDITOR_ID")
        super().__init__(editor_id, prompt, thread)
