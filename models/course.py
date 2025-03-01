from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And
from marshmallow.fields import String  , Email


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))  
    teacher = db.relationship('Teacher') 

class CourseSchema(ma.Schema):
    name = String(required=True, validate=And(
        Length(min=5, error='Name must be at least 5 characters long'),
        Regexp('^[A-Za-z]$', error='Name must contain only letters')        
    ))
    
    teacher = fields.Nested('TeacherSchema')
    class Meta:
        fields = ('id', 'name', 'start_date', 'end_date', 'teacher_id')


one_course = CourseSchema()
many_courses = CourseSchema(many=True)
course_without_id = CourseSchema(exclude=['id'])
