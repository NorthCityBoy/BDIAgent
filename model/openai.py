from openai import OpenAI
import os
from dotenv import load_dotenv
import datetime
import json

from agent.agent import Agent


class OpenAIModel:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_API_BASE")
        )

    def get(self, agent: Agent):
        # 创建或使用现有的线程
        if not agent.thread:
            agent.thread = self.client.beta.threads.create().id

        message = self.client.beta.threads.messages.create(
            thread_id=agent.thread,
            role="user",
            content=agent.prompt
        )

        run = self.client.beta.threads.runs.create(
            thread_id=agent.thread,
            assistant_id=agent.editor_id
        )

        while not run.completed_at:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=agent.thread,
                run_id=run.id
            )

        messages = self.client.beta.threads.messages.list(
            thread_id=agent.thread
        )

        outline = messages.data[0].content[0].text.value
        # 保存消息数据
        self._save_messages_data(agent, outline)

        return outline

    def _save_messages_data(self, agent: Agent, messages):

        directory_path = "data/"

        # 创建子文件夹
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # 保存数据到文件
        file_path = f"{directory_path}/{agent.editor_id}.json"
        with open(file_path, "a") as file:
            file.write(messages)
