from pydantic import BaseModel, EmailStr, ValidationError
from typing import List

class Item(BaseModel):
    name: str
    description: str

class User(BaseModel):
    name: str
    email: EmailStr
    items: List[Item]

try:
    user = User(
        name="Alex",
        email="alex@example.com",
        items=[
            {"name": "Item 1", "description": "Description 1"},
            {"name": "Item 2", "description": "Description 2"}
        ]
    )
    print("User model is valid:", user)
except ValidationError as e:
    print("Validation error:", e)
