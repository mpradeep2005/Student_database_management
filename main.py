from fastapi import FastAPI

from model import Students

app=FastAPI()
student_lis=[

]


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