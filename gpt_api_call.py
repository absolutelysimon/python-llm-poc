# pip install ollama
# from .gpt_api_call import call_gpt
from ollama import Client

server_ip = 'http://198.166.143.190:11434'  # GPT API Endpoint
gpt_model = 'qwen2.5-coder'  # General GPT "llama3.1"


def call_gpt(prompt):
    client = Client(host=server_ip)
    response = client.chat(model='llama3.1', messages=[
        {'role': 'user', 'content': prompt},])

    return response['message']['content']
