from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Azure 🚀</h1>
    <p>This site is running on Python 3.14 GOD BLESS STATES</p>
    """

if __name__ == "__main__":
    app.run()
