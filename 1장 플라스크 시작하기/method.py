from flask import Flask

app = Flask(__name__)

@app.route('/login', methods = ['GET'])
def login_page():
    return show_the_login_form()

@app.route('/login', methods = ['GET', 'POST'])
def login():
	return do_the_login()
