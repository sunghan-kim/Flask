# cookie

from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/get")
def get_cookie():
    username = request.cookies.get('username')
    return render_template('variable.html', name=username)

@app.route("/add/<user>")
def add_cookie(user):
    resp = make_response(render_template('simple.html', name=user))
    resp.set_cookie('username', user)
    return resp

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")
