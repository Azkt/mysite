


from flask import Flask
from flask import render_template
import constants
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.Integer)
    name = db.Column(db.String(80))
    teacher_name = db.Column(db.String(80))
    resource_name = db.Column(db.String(80))
    resource_url = db.Column(db.String(300))

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
    courses = Course.query.all()
    return render_template('class_schedule.html',
                           courses=courses)

@app.route('/register')
def register():
    return render_template('register.html',
                            courses=constants.COURSES)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/top_ten_songs')
def top_ten_songs():
    return render_template('top_ten_songs.html', songs=constants.TOP_TEN_SONGS)

if __name__ == '__main__':
  db.create_all()
