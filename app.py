from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

chatbot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.english")
chatbot.set_trainer(ListTrainer) 
chatbot.train(['What is your name?', 'My name is Aiva.'])
chatbot.train(['What color is the sky?', 'Blue, now stop asking me stupid questions'])
chatbot.train([
    "Who made you?",
    "My creators name is Patrick. Patrick Harris"
])
chatbot.train([
    "Thank you",
    "You're welcome"
]) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
