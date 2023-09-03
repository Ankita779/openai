from textbase import bot, Message
from textbase.models import openai
from typing import List

# Load your OpenAI API key

openai.api_key ="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"

# Prompt for GPT-3.5 Turbo
Message=[]
SYSTEM_PROMPT=input("what type of chatbot would you like to create?\n")
Message.append({"role":"system","content":SYSTEM_PROMPT})
print("Assistance is ready!")
while input!="quit()":
    message=input("")
    Message.append({"role":"user","content":"message"})
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        Message=Message
    )
    reply=response["choices"][0]["Message"]["content"]
    Message.append({"role":"assistant","content":reply})
    print("\n" + reply + "\n")

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = openai.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }