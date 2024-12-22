from pydantic import BaseModel, EmailStr, ValidationError

class UserInput(BaseModel):
    name: str
    email: EmailStr
    age: int
try:
    user = UserInput(
        name="Alex",
        email="alex@example.com",
        age="22"
    )
except ValidationError as e:
    print(e.json())

print(user.dict())


