from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
import uvicorn

# Database Configuration
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Password Hashing Configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Models (SQLAlchemy)
class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  full_name = Column(String, nullable=True)


# Create Database Tables
Base.metadata.create_all(bind=engine)


# Schemas (Pydantic)
class UserBase(BaseModel):
  email: EmailStr
  full_name: str | None = None


class UserCreate(UserBase):
  password: str


class UserOut(UserBase):
  id: int

  class Config:
    orm_mode = True


# CRUD Operations
def get_user_by_email(db: Session, email: str):
  return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
  hashed_password = pwd_context.hash(user.password)
  db_user = User(email=user.email, hashed_password=hashed_password, full_name=user.full_name)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user


# FastAPI Initialization
app = FastAPI()


# Dependency for Database Session
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


# Routes
@app.post("/users/", response_model=UserOut, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
  db_user = get_user_by_email(db, email=user.email)
  if db_user:
    raise HTTPException(status_code=400, detail="Email already registered")
  return create_user(db=db, user=user)


if __name__ == "__main__":
  uvicorn.run("main10_2_3:app", host="127.0.0.1", reload=True)
