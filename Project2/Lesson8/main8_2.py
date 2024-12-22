from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., example="Coffee", description="The name of the item")
    description: str = Field(None, example="A hot, stimulating drink", description="A detailed description of the item")
    price: float = Field(..., gt=0, description="The price of the item must be greater than zero")
    tax: float = Field(None, gt=0, description="The tax on the item, if applicable")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Coffee",
                "description": "Black hot coffee",
                "price": 2.99,
                "tax": 0.3,
            }
        }


item = Item(name="Coffee", description="Black hot coffee", price=2.99, tax=0.3)


print(item.model_dump_json())
