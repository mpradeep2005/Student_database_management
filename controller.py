import model,schema
from sqlalchemy.orm import Session

def get_all_students(db:Session):
    return db.query(model.Students).all()

def add_students(db:Session,student:schema.Students_create):
    status=model.Students(**student.model_dump())
    db.add(status)
    db.commit()
    db.refresh(status)
    return "Added"


def update_student(db:Session,id:int, student:schema.Students_create):
    status=db.query(model.Students).filter(id == model.Students.id).first()
    if status:
        for key,value in student.model_dump().items():
            setattr(status,key,value)
        db.commit()
        db.refresh(status)
        return"Updated student"
    return "invalid student id"

def delete_student(db:Session, id:int):
    status=db.query(model.Students).filter(id == model.Students.id).first()
    if status:
        db.delete(status)
        db.commit()
        return "Deleted Successfully"
    return "invalid student id"


def get_students_byId(id:int,db:Session):
    status = db.query(model.Students).filter(id == model.Students.id).first()
    return status