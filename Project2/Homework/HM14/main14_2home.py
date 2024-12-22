from fastapi import FastAPI, BackgroundTasks
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import uvicorn

app = FastAPI()


def send_email(to_email: str, subject: str, message: str):
    sender_email = "op663246@gmail.com"
    sender_password = "o01102008p"


    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email


    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def log_user_action(user_id: int, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] User {user_id}: {action}\n"
    with open("user_actions.log", "a") as log_file:
        log_file.write(log_entry)
    print(f"Action logged for user {user_id}")


@app.post("/send-email/")
async def send_email_endpoint(
    background_tasks: BackgroundTasks,
    to_email: str,
    subject: str,
    message: str
):
    background_tasks.add_task(send_email, to_email, subject, message)
    return {"message": f"Email to {to_email} is being sent in the background"}


@app.post("/log-action/")
async def log_action_endpoint(
    background_tasks: BackgroundTasks,
    user_id: int,
    action: str
):
    background_tasks.add_task(log_user_action, user_id, action)
    return {"message": f"Action '{action}' for user {user_id} is being logged in the background"}



if __name__ == "__main__":
  uvicorn.run("main14_2home:app", host="127.0.0.1", reload=True)