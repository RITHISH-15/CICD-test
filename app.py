
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hey Rithish, Welcome! 👋</h1>
    <p>My first CI/CD website is working.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
