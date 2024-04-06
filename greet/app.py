from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def show_welcome ():
    return 'welcome'

@app.route('/welcome/home')
def show_welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def show_welcome_back():
    return 'welcome back'