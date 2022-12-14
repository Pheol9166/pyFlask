# source: https://hleecaster.com/flask-introduction/

from flask import Flask

# flask 사용
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return """
    <h1> 이건 h1 제목 </h1>
    <p> 이건 p 본문 </p>
    <a href = "https://flask.palletsprojects.com">Flask 홈페이지 바로 가기</a>
    """

# 동적 URL
# string이 기본값
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name: str, user_id: int):
    return f"Hello, {user_name} ({user_id})!"


if __name__ == "__main__":
    app.run(debug=True)


