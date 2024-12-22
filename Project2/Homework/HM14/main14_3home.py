from fastapi import FastAPI, BackgroundTasks
import uvicorn

app = FastAPI()

def write_log(message: str):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")
    print(message)

@app.get("/send-email/")
async def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Sending email in background")
    return {"message": "Email is being sent in background"}



if __name__ == "__main__":
  uvicorn.run("main14_3home:app", host="127.0.0.1", reload=True)