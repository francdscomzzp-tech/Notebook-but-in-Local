from ollama import chat
from ollama import ChatResponse

message = input("domanda per AI:")

class AI:   
    response: ChatResponse = chat(
        model ='gemma4',
        messages= [
            {
                'role': 'user',
                'content': message,
            },
        ],
    )
    print(response['message']['content'])
    print(response.message.content)