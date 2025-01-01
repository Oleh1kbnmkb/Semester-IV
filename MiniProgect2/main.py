from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import uvicorn


DATABASE_URL = "sqlite:///./items.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


app = FastAPI(
    title="InfoHub",
    description="InfoHub for managing and securing information.",
    version="1.0.0",
)


class ItemDB(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    available = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    available: bool = True

    class Config:
        orm_mode = True


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


users_db = {
    "admin": {"password": pwd_context.hash("adminpassword")},
    "user2": {"password": pwd_context.hash("password2")},
}


security_basic = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@app.get("/basic-auth", tags=["Authentication"], summary="Basic Authentication Endpoint")
def basic_auth(credentials: HTTPBasicCredentials = Depends(security_basic)):
    user = users_db.get(credentials.username)
    if not user or not pwd_context.verify(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {"message": f"Welcome, {credentials.username}!"}



@app.post("/token", tags=["Authentication"], summary="Generate OAuth2 Token")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    return {"access_token": form_data.username, "token_type": "bearer"}



@app.get("/items/", response_model=List[Item], tags=["Items"], summary="List All Items")
def list_items(db: Session = Depends(get_db)):
    items = db.query(ItemDB).all()
    return items


@app.get("/items/{item_id}", response_model=Item, tags=["Items"], summary="Get Item by ID")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items/", response_model=Item, tags=["Items"], summary="Create Item")
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemDB(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item




@app.delete("/items/{item_id}", tags=["Items"], summary="Delete Item")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Item {item_id} deleted"}




if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", reload=True)