# REST API 구현
# - 특정한 URI를 요청하면 JSON 형식으로 데이터를 반환하도록 만들면 됨
# - Flask에서는 dictionary 데이터를 응답 데이터를 만들고,
#   이를 jsonify() 메서드를 활용해서 JSON 응답 데이터로 만들 수 있음
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/json_test")
def hello_json():
    data = {
        "name": "Aaron",
        "family": "Byun"
    }
    return jsonify(data)

@app.route("/server_info")
def server_json():
    data = {
        "server_name": "127.0.0.1",
        "server_port": "8081"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8081")
