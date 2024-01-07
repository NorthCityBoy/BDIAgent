import json

from agent.editor_agent import Editor
from agent.executive_editor_agent import ExecutiveEditor
from model.openai import OpenAIModel

prompt = "我叫石帅，武学天才，但是现在没有任何功力，请你设计个剧情让我打败情敌杨过，在金庸的武侠世界中迎娶小龙女。"
model = OpenAIModel()

editor = Editor(prompt=prompt)
# outline = model.get(editor)
# print(outline)

editor_id = editor.editor_id
outline_path = f"data/{editor_id}.json"
with open(outline_path, 'r') as file:
    data = json.load(file)

title = data["标题"]
roles = data["核心角色"]
summery = data["剧情概要"]
chapters = []
for key, value in data["章节划分"].items():
    chapters.append({key: value})
prompt = str(title) + "\n" + str(roles) + "\n" + str(summery) + "\n"

events = []
for i in range(len(chapters)):
    exe_editor = ExecutiveEditor(prompt=prompt + str(chapters[i]))
    chapter = model.get(exe_editor)
    print(chapter)
