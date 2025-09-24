from pydantic import BaseModel
class Students_create(BaseModel):
    Reg_no:int
    Name:str
    Class_Name:str
    Mobile_no:str
    CGPA:float

class Students_respones(Students_create):
    id:int

    class config:
        orm_mode=True