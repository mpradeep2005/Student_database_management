from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:2005@localhost:7070/Students Records")
session_local=sessionmaker(autoflush=False,
                           autocommit=False,
                           bind=engine)

def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()