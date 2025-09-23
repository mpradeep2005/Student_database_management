from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

import controller
from DB_connection import get_db, engine
from model import Base
from schema import Students

app=FastAPI()
Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return "uvicorn is running"

@app.get("/students")
def get_all_students(db:Session=Depends(get_db)):
    return controller.get_all_students(db)

@app.get("/student/{id}")
def get_student_by_id(id:int,db:Session=Depends(get_db)):
    return controller.get_students_byId(id,db)

@app.post("/student")
def add_student(student:Students,db:Session=Depends(get_db),):
    controller.add_students(db,student)
    return "Added successfully"

@app.put("/student/{id}")
def update_student(id:int,update_student:Students,db:Session=Depends(get_db),):
    controller.update_student(db,id,update_student)

@app.delete("/student")
def delete_student(id:int,db:Session=Depends(get_db),):
    controller.delete_student(db,id)


