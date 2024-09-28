# pip install ollama
# from .gpt_api_call import call_gpt
from ollama import Client

server_ip = 'http://198.166.143.190:11434'

# gpt_model = 'llama3.1'  # ChatGPT equivalent
gpt_model = 'qwen2.5-coder'  # More optimised for code


def call_gpt(prompt):
    client = Client(host=server_ip)
    response = client.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response['message']['content']


if __name__ == '__main__':
    user_prompt = 'Why is the sky blue?'
    print(call_gpt(user_prompt))
