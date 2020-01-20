from application import app
from application import greetings


@app.route('/')
@app.route('/index')
def hello_world():
    return greetings.greet(mode='name')


if __name__ == '__main__':
    app.run()
