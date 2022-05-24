# Flask 객체 임포트, 이클래스의 인스턴스는 WSGI 애플리케이션을 만들어 줍니다.
from flask import Flask 

#Flask 객체의 인자로 __name__이 들어간다. 해당 인자는 정적 파일과 템플릿을 찾는데 쓰인다.
app = Flask(__name__)

# route 데이코레이션을 사용해url 생성
@app.route('/index')
# route는 중첩 가능
@app.route('/')
def hello_world():
return 'Hello, World'
