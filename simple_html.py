# 웹페이지 구현
# - 특정 웹주소(URI)를 접속하면 웹페이지를 보여주면 됨
# - 서버는 요청을 받아, 적절한 처리를 한 뒤 html 반환
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/html_test")
def hello_html():
    # html file은 templates 폴더에 위치
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8081")
