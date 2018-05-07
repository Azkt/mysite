# Run this script by typing the following in a Bash console:
# python database_import_courses.py

from flask_app import db
from flask_app import Course
import constants

for course in constants.COURSES:
    db.session.add(
        Course(
            period=course.period,
            name=course.name,
            teacher_name=course.teacher_name,
            resource_name=course.resource_name,
            resource_url=course.resource_url))

db.session.commit()