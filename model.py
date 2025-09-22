from pydantic import BaseModel
class Students(BaseModel):
    id:int
    Reg_no:int
    Name:str
    Class_Name:str
    Mobile_no:int
    CGPA:float