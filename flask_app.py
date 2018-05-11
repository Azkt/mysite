from flask import Flask
from flask import render_template
import constants
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)
Bootstrap(app)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.Integer)
    name = db.Column(db.String(80))
    teacher_name = db.Column(db.String(80))
    resource_name = db.Column(db.String(80))
    resource_url = db.Column(db.String(300))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    artist_name = db.Column(db.String(80))
    youtube_url = db.Column(db.String(300))

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
    songs = Song.query.all()
    return render_template('top_ten_songs.html',
                           songs=songs)

nav = Nav(app)
@nav.navigation('mysite_navbar')
def create_navbar():
    home_view = View('Home', 'index')
    register_view = View('Register', 'register')
    about_me_view = View('About Me', 'about_me')
    class_schedule_view = View('Class Schedule', 'class_schedule')
    top_ten_songs_view = View('Top Ten Songs', 'top_ten_songs')
    misc_subgroup = Subgroup('Misc',
                             about_me_view,
                             class_schedule_view,
                             top_ten_songs_view)
    return Navbar('MySite', home_view, misc_subgroup, register_view)

if __name__ == '__main__':
  db.create_all()