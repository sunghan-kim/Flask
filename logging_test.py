# 로깅(logging)
# - 로깅 정보는 로그의 레벨에 따라서 출력을 제한할 수 있다.
# - DEBUG > INFO > WARNING > ERROR > Critical

from flask import Flask
import requests

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>", 404

@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
