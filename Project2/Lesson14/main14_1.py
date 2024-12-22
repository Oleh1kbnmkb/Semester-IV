from fastapi import FastAPI, BackgroundTasks
import asyncio
import uvicorn

app = FastAPI()

async def send_email(email: str):
    await asyncio.sleep(2)
    print(f"Email sent to {email}")

@app.post("/send-email/")
async def send_email_endpoint(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(send_email, email)
    return {"message": "Email sending in the background"}

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with async tasks"}



if __name__ == "__main__":
  uvicorn.run("main14_1:app", host="127.0.0.1", reload=True)