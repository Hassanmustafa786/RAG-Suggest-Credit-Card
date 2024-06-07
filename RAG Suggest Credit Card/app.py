# app.py
from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, download_loader
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

SimpleWebPageReader = download_loader("SimpleWebPageReader")

loader = SimpleWebPageReader()
documents = loader.load_data(urls=["https://www.mymoneysouq.com/cards/compare-credit-cards-uae"])

index = VectorStoreIndex.from_documents(documents)
chat_engine = index.as_chat_engine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggest_credit_card', methods=['POST'])
def suggest_credit_card():
    data = request.get_json()
    message = data['message']
    response = chat_engine.chat(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)