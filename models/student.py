from init import db,ma
class Student(db.model):    #inherit db.Model "db" defined in init.py as SQLAlchemy()
    __tablename__ = "students"
    
    id = db.Column(db.Integer, primary_key=True) 
    
    name = db.Column(db.String(100), nullable=False)   
    email = db.Column(db.String(200), nullable=False, unique=True)  
    address = db.Column(db.String(500))
    
    
class StudentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email","address")
        
many_studemts = StudentSchema(many=True)  
one_student =   StudentSchema()  