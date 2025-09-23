from pydantic import BaseModel
class Students(BaseModel):
    Reg_no:int
    Name:str
    Class_Name:str
    Mobile_no:str
    CGPA:float