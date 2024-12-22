from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/calculate/")
def perform_calculation(num1: float, num2: float, operation: str):
    if operation == "add":
        return {"result": num1 + num2}
    elif operation == "subtract":
        return {"result": num1 - num2}
    elif operation == "multiply":
        return {"result": num1 * num2}
    elif operation == "divide":
        if num2 != 0:
            return {"result": num1 / num2}
        else:
            return {"error": "Division by zero"}
    else:
        return {"error": "Invalid operation"}



if __name__ == "__main__":
  uvicorn.run("main4_3:app", host="127.0.0.1", reload=True)