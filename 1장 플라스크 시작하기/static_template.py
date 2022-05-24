from flask import Flask, render_template

#Flask 객체에 static_folder와 template_folder를 지정해준다.
app = Flask(__name__, static_folder = 'static', template_folder = 'templates')

#tatic_folder를 지정해주면 /static URL로 접근할 수 있다.
#template_folder를 지정해주면 render_template에서 해당 템플릿 파일을 찾을 수 있다.
@app.route('/hello')
def hello():
        return render_template('hello.html')
