from pydantic import BaseModel, ValidationError
from typing import List

class Item(BaseModel):
    name: str
    description: str
    price: float

class ItemList(BaseModel):
    items: List[Item]

data_to_validate = {
    "items": [
        {"name": "Apple", "description": "Fruit", "price": 0.5},
        {"name": "Orange", "description": "Fruit", "price": 0.8},
        {"name": "Banana", "description": "Fruit", "price": "unknown"}
    ]
}

try:
    validated_data = ItemList.model_validate(data_to_validate)
    print(validated_data)
except ValidationError as e:
    print("Помилки валідації:")
    print(e.json())
