from flask import Flask

app = Flask(__name__)


@app.route("/set/dataset")
def set_dataset():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=True)
