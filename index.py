from flask import Flask, jsonify
from config import Config

app = Flask(__name__)
config = Config()


@app.route("/")
def index():
    return jsonify(message="Hello from Flask on Vercel!")
