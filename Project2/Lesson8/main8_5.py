from pydantic import BaseModel
from typing import Optional
import json


class User(BaseModel):
  id: int
  name: str
  age: Optional[int] = None

  class Config:
    from_attributes = True


json_str = '{"id": 1, "name": "John", "age": 30}'
user = User.model_validate_json(json_str)

user_dict = {"id": 2, "name": "Jane", "age": 25}
user_from_dict = User.model_validate(user_dict)


class ORMUser:
  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age


orm_user = ORMUser(id=3, name="Dave", age=40)
user_from_orm = User.model_validate(orm_user)

print(user.json())
print(user_from_dict.json())
print(user_from_orm.json())
