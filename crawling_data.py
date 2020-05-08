# 크롤링 데이터 반환
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
