from flask import Flask, request, jsonify, render_template
import sqlite3
from chatbot_model import get_chat_response
import os

app = Flask(__name__)

# Serve the HTML file
@app.route("/")
def index():
    return render_template("chat.html")  # Assumes chat.html is in a folder named 'templates'

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data["message"]
    bot_response = get_chat_response(user_input)
    log_interaction(user_input, bot_response)
    return jsonify({"response": bot_response})

def log_interaction(user_input, bot_response):
    conn = sqlite3.connect('chat_logs.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (user_input TEXT, bot_response TEXT)')
    cursor.execute('INSERT INTO logs (user_input, bot_response) VALUES (?, ?)', (user_input, bot_response))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)
