# source: https://m.blog.naver.com/mksun8472/221552004899
from flask import Flask

app = Flask(__name__)

# routing
@app.route('/') # '/'로 접속했을 때, 반응할 함수 실행
def hello():
    return 'Hello World!'

@app.route('/login')
def login():
    return 'hello, login'

if __name__ == "__main__":
    app.run(debug=True)