from pydantic import BaseModel
class Students(BaseModel):
    Reg_no:int
    Name:str
    Class:str
    Mobile_no:int
    CGPA:float