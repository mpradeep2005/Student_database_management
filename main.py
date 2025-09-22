from fastapi import FastAPI

from model import Students

app=FastAPI()

student_lis=[]

@app.get("/")
def root():
    return "uvicorn is running"

@app.get("/students")
def get_all_students():
    return student_lis

@app.post("/student")
def add_student(student:Students):
    student_lis.append(student)
    return student

@app.put("/student/{id}")
def update_student(id:int,update_student:Students):
    for index,student in enumerate(student_lis):
        if student_lis[index]==id:
            student_lis[index]=update_student
        return "updated"
    return "Invalid student id"

@app.delete("/student")
def delete_student(id:int):
    for index, student in enumerate(student_lis):
        if student_lis[index] == id:
            del student_lis[index]
        return "deleted"
    return "Invalid student id"


