# app.py baseline 코드

from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    return "test"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
