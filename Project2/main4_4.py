import math
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/add/{num1}/{num2}/")
def add(num1: float, num2: float):
    return {"result": num1 + num2}

@app.get("/subtract/{num1}/{num2}/")
def subtract(num1: float, num2: float):
    return {"result": num1 - num2}

@app.get("/multiply/{num1}/{num2}/")
def multiply(num1: float, num2: float):
    return {"result": num1 * num2}

@app.get("/divide/{num1}/{num2}/")
def divide(num1: float, num2: float):
    if num2 != 0:
        return {"result": num1 / num2}
    else:
        return {"error": "Division by zero"}

@app.get("/sqrt/{num}/")
def sqrt(num: float):
    return {"result": math.sqrt(num)}

@app.get("/square/{num}/")
def square(num: float):
    return {"result": num ** 2}



if __name__ == "__main__":
  uvicorn.run("main4_4:app", host="127.0.0.1", reload=True)