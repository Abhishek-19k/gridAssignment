from email import parser
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from typing import List
from user import User, UserCreate, UserDB, Base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables if they don't exist already
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/users", response_model=List[User] | dict)
async def get_users(first_name: str, db: Session = Depends(get_db)):
    users = db.query(UserDB).filter(UserDB.first_name.like(f'{first_name}%')).all()
    if users:
        return users
    else:
        response = requests.get(f"https://dummyjson.com/users/search?q={first_name}")
        if response.status_code == 200:
            res = response.json()
            print(res)
            return res
        else:
            raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_dict = user.dict()
    db_user = UserDB(**user_dict)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
