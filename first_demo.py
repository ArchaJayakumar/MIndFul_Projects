from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Students = {
    1 : {
        "name" : "Archa",
        "age" : 20,
        "dept" : "CST"
    }
}

class Student(BaseModel):
    name : str
    age : int
    dept : str

@app.get("/")
async def root():
    return "This is home page"

@app.get("/get-Student/{stu_id}")
async def getStu(stu_id : int):
    return Students[stu_id]

@app.get("/get-by-name")
async def getStu(name : str):
    for stu_id in Students:
        if Students[stu_id]["name"] == name:
            return Students[stu_id]
    return {"Data" : "Not Found"}

@app.post("/createStudent/{stu_id}")
async def create_Stu(stu_id : int, student : Student):
    if stu_id in Students:
        return {"Error" : "Student Already Exist"}
    Students[stu_id] = student
    return Students[stu_id]

@app.put("/updateStudent/{stu_id}")
async def update_Stu(stu_id: int , student : Student):
    if stu_id not in Students:
        return {"Error" : "Student not Exist"}
    
    if student.name != None:
        Students[stu_id].name = student.name

    if student.age != None:
        Students[stu_id].age = student.age

    if student.dept != None:
        Students[stu_id].dept = student.dept

    return Students[stu_id]

@app.delete("/deleteStudent/{stu_id}")
async def delete_Student(stu_id : int):
    if stu_id not in Students:
        return {"Error" : "Student does not Exit"}
    
    del Students[stu_id]
    return {"Message" : "Deleted"}
