from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from datetime import date

Base = declarative_base()

class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String)
    birth_date = Column(Date)
    phone = Column(String)

class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    email: str
    birth_date: date
    phone: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
