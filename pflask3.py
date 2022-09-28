# source: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=mksun8472&logNo=221552606651
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/child')
def child():
    return render_template('child.html')

if __name__ == "__main__":
    app.run(debug=True)
