from typing import List

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

import controller
import schema
from DB_connection import get_db, engine
from model import Base
from schema import Students_create

app=FastAPI()
Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return "uvicorn is running"

@app.get("/students",response_model=List[schema.Students_respones])
def get_all_students(db:Session=Depends(get_db)):
    return controller.get_all_students(db)

@app.get("/student/{id}",response_model=schema.Students_respones)
def get_student_by_id(id:int,db:Session=Depends(get_db)):
    return controller.get_students_byId(id,db)

@app.post("/student")
def add_student(student:Students_create,db:Session=Depends(get_db),):
    controller.add_students(db,student)
    return "Added successfully"

@app.put("/student/{id}")
def update_student(id:int,update_student:Students_create,db:Session=Depends(get_db),):
    controller.update_student(db,id,update_student)
    return "Updated Successfully"

@app.delete("/student/{id}")
def delete_student(id:int,db:Session=Depends(get_db),):
    controller.delete_student(db,id)
    return "Deleted successfully"

