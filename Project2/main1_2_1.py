from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/greet/")
def read_greeting(name: str = Query(None, description="Введіть ваше ім'я")):
    return {"message": f"Вітаємо {name}!"}



@app.get("/greet/{name}")
def read_greeting(name: str):
    return {"message": f"Вітаємо, {name}!"}



@app.get("/calc/")
def read_greeting(operation: str, num1: float, num2: float):
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "/":
    result = num1 // num2
  elif operation == "*":
    result = num1 * num2
  return {
    "operation": operation,
    "num1": num1,
    "num2": num2,
    "result": result,
  }







if __name__ == "__main__":
  uvicorn.run("main1_2_1:app", host="127.0.0.1", reload=True)