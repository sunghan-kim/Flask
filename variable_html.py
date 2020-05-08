# 웹페이지(HTML)를 파이썬 flask로 만들기
# - flask 프로그래밍 로직에 따라 HTML 태그를 만들거나, HTML 내용을 채우기 위해
#   Jinja2 템플릿 엔진을 사용
# - jinja2 engine을 사용하여 탬플릿을 만들고 템플릿 안의 값을 채워서 랜더링한다.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html', name=user) # name : html 파일의 변수명

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
