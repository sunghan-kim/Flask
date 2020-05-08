# Flask 부트스트랩(Bootstrap) 사용

# Reference : http://blog.naver.com/PostView.nhn?blogId=cosmosjs&logNo=221034005787&categoryNo=0&parentCategoryNo=56&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search

# 설치 : pip install flask-bootstrap

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/bootstrap")
def bootstrap():
    return render_template('bootstrap.html')

if __name__ == "__main__":
    app.run("127.0.0.1", debug=True)
