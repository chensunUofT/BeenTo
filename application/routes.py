from flask import render_template
from application import app
from application import greetings
from application.get_user_ip_location import get_ip, get_location

@app.route('/')
@app.route('/index')
def hello_world():
    ip = get_ip()
    location_json = get_location(ip)
    city = location_json['city']
    greeting_text = greetings.greet(mode='name', name='user from {}'.format(city))
    return render_template('homepage.html', greeting_text = greeting_text)


if __name__ == '__main__':
    app.run()
