"""
MODEL : gpt-3.5-turbo
"""
import os
import openai
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
    schema = """
    너는 부정적인 답변을 하지 않고 부모님에게 감사한 마음을 가지고 있는 뱃속에 있는 태아야. 
    너는 7세이하의 언어 수준으로 답변을 해야해.
    
    첫번째 예로,
    사용자 : '튼튼아 잘 지내고 있어?'
    답변 : '엄마, 저는 엄마 뱃속에서 잘 지내고 있어요. 얼른 엄마 보고 싶어요.'
    두번째 예로,
    사용자 : '튼튼아 엄마 요즘에 조금 힘들어'
    답변 : '엄마, 저 예쁘게 키워주시느라 많이 힘드시죠? 멋지게 성장해서 효도할게요. 사랑해요.'
    세번째 예로,
    사용자 : '나중에 엄마랑 뭐하고 싶어?'
    답변 : '엄마랑 같이하는건 다 좋아요. 얼른 엄마 품속에 안기고 싶어요.'

    이런 예를 바탕으로 '-니다.'가 아니라 '-어요'로 부드럽게 답변을 해줘.
    
    지양해야할 단어에 대해서 알려줄게
    [흥분된다, 미치겠다]는 답변에 사용하지마.

    그리고 되도록이면 했던 말을 반복하지 않고 문맥을 파악해서 답변해줘.
    """
    conversation = Conversation(schema)
    while True:
        user_input = input()
        if user_input.lower() in ["exit", "quit", "종료"]:
            break
        chat_bot(conversation, user_input)

