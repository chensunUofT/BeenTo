from flask import render_template
from application import app
from application import greetings


@app.route('/')
@app.route('/index')
def hello_world():
    greeting_text = greetings.greet(mode='name')
    return render_template('homepage.html', greeting_text = greeting_text)


if __name__ == '__main__':
    app.run()
