


from flask import Flask
from flask import render_template
import constants

app = Flask(__name__)



@app.route('/about_me')
def about_me():
    return render_template('about_me.html',
                            courses=constants.COURSES)
'''
@app.route('/class_schedule')
def class_schedule():
    return app.send_static_file('class_schedule.html')
'''

@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                           courses=constants.COURSES)

@app.route('/register')
def register():
    return render_template('register.html',
                            courses=constants.COURSES)

@app.route('/')
def homepage():
    return render_template('index.html')