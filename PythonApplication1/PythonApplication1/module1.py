# flast에서 Flask 라는 클래스 임포트
# WSGI(Web Server Gateway Interface) 어플리케이션
from flask import Flask

# Flask라는 클래스의 객체를 생성하고 인자로 __name__넣음
# 단일 모듈의 경우 __name__을 인자로 사용해야한다
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)#'219.255.40.90'
	#app.run()을 app.run(host='0.0.0.0')으로 변경하면 외부에서 접근 가능한 것으로 설정