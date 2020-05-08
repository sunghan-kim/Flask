# HTTP 상태 에러(error) 처리
# - errorhandler를 사용하여 HTTP 오류 코드가 나오는 페이지를 정의할 수 있음
# - return의 두 번째 인자로 에러코드를 넘겨주지 않으면 성공(200)으로 인지함

from flask import Flask
import requests

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404


@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
