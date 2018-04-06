from flask import Flask, render_template, request
from pymongo import MongoClient

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


app = Flask(__name__)
client = MongoClient('localhost', 5000)


chatbot = ChatBot(
    "AIVA",
    storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
    database = "aiva_db",
    database_uri = 'mongodb://localhost:5000',
    logic_adapters =[
        'chatterbot.logic.BestMatch'
    ],
    filters =[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter'
) 

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

print('Chatbot Started: ') 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()

