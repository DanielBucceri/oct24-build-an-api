from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from init import db
from models.student import Student, many_students, one_student, student_without_id

students_bp = Blueprint("students", __name__)

#read all - Get /students
@students_bp.route('/students')
def get_all_students():
    stmt = db.select(Student)
    students = db.session.scalars(stmt)
    return many_students.dump(students)

 #Read one - GET /Students/int:stu id
@students_bp.route('/students/<int:student_id>')
def get_one_student(student_id):
     stmt = db.select(Student).filter_by(id=student_id) 
     student = db.session.scalar(stmt)
     if student:
         return one_student.dump(student)
     else:
         return {'error': f'Student with id {student_id} does not exist'}, 404
     
#Create - POST /Students
@students_bp.route('/students', methods=['POST'])
def create_student(student_id):
    try:
        data = student_without_id.load(request.json)
        new_student = Student(
            name=data.get('name'),
            email=data.get('email'),
            address=data.get('address')
            )
        db.session.add(new_student)
        db.session.commit()

        return get_one_student.dump(new_student)
    except IntegrityError as err:
        if err.orig.pgcode == 23505:
            return {"error":"Email address already in use"}, 409 # conflict
        elif err.orig.pgcode == 23502:
            return {"error":"Field is required "}, 400
        
        
    # Get incomeing request body (JSON)
    # Create a new isntance of student model
    # Add the intance to the db session
    # Commit the session
    # Return the new student isntance



# update - PUT  /students/<int:id>
# delete - DELETE /students/<int:id>