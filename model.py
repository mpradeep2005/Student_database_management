from sqlalchemy import Integer, String, Float, Column
from sqlalchemy.orm import declarative_base
Base=declarative_base()
class Students(Base):
    __tablename__="Students Records"
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    Reg_no=Column(Integer,unique=True)
    Name=Column(String)
    Class_Name= Column(String)
    Mobile_no=Column(String,unique=True)
    CGPA=Column(Float)