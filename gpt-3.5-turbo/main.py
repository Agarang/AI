"""
MODEL : gpt-3.5-turbo
"""
import os
import openai
from schema import SCHEMA
from key import OPENAI_API_KEY

class Conversation:
    def __init__(self, schema):
        self.messages = [{'role': 'system', 'content': schema}]
    
    def add_user_input(self, user_input):
        self.messages.append({'role': 'user', 'content': user_input})
    
    def add_bot_response(self, response):
        self.messages.append({'role': 'assistant', 'content': response})

def generate_answer(messages, model_gpt="gpt-3.5-turbo"):
    answer_result = {}
    openai.api_key = OPENAI_API_KEY

    try:
        response = openai.ChatCompletion.create(
            model=model_gpt,
            messages=messages
        )
        answer_result['answer'] = response.choices[0].message['content'].strip()
    except Exception as err:
        print("[ERROR][GENERATE_ANSWER] : ", str(err))
        answer_result['answer'] = "죄송합니다. 답변을 생성하는 데 문제가 발생했습니다."

    return answer_result['answer']

def chat_bot(conversation, user_input):
    conversation.add_user_input(user_input)
    response = generate_answer(conversation.messages)
    conversation.add_bot_response(response)
    print(response)
    return response

if __name__ == '__main__':
    conversation = Conversation(SCHEMA)
    while True:
        user_input = input()
        if user_input.lower() in ["exit", "quit", "종료"]:
            break
        chat_bot(conversation, user_input)

