from flask import Flask, url_for

app = Flask(__name__)

# app 객체를 이용해 라우팅 경로 설정
# 해당 라우팅 경로로 요청이 올 때 실행할 함수를 바로 밑에 작성
@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/hello")
def hello_flask():
    return "<h1>Hello Flask!</h1>"

@app.route("/first")
def hello_first():
    return "<h3>Hello First!</h3>"

# URI 변수 사용
@app.route("/profile/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"

# URI 변수 데이터 타입 지정
@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id

@app.route("/first/<int:messageid>")
def get_first_message(messageid):
    return "<h1>%d</h1>" % (messageid + 5)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8081")
