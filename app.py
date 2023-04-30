#some changes has been made and further testing will be done as soon as possible
#maintaining streak for the github don't know why it's not getting added
import os
import re
from threading import Timer

from revChatGPT.revChatGPT import Chatbot
from slack_bolt import App

SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']

app = App(token=SLACK_BOT_TOKEN)

# Listen for an event from the Events API
@app.event("app_mention")
def event_test(event, say):
    ChatGPTConfig = {
        "email": os.environ['CHATGPT_EMAIL'],
        "password": os.environ['CHATGPT_PASSWORD']
    }
    chatbot = Chatbot(ChatGPTConfig, conversation_id=None)
    
    prompt = re.sub('(?:\s)<@[^, ]*|(?:^)<@[^, ]*', '', event['text'])
    try:
        response = chatbot.get_chat_response(prompt)
        user = event['user']
        user = f"<@{user}> you asked:"
        asked = ['>',prompt]
        asked = "".join(asked)
        send = [user,asked,response["message"]]
        send = "\n".join(send)
    except Exception as e:
        send = "We're experiencing exceptionally high demand. Please, try again."
    say(send)

def chatgpt_refresh():
    ChatGPTConfig = {
        "email": os.environ['CHATGPT_EMAIL'],
        "password": os.environ['CHATGPT_PASSWORD']
    }
    chatbot = Chatbot(ChatGPTConfig, conversation_id=None)
    chatbot.refresh_session()
    Timer(60, chatgpt_refresh).start()

if __name__ == "__main__":
    Timer(60, chatgpt_refresh).start()
    app.start(4000)  # POST http://localhost:4000/slack/events
