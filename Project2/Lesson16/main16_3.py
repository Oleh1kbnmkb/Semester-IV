from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import uvicorn
import jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_jwt(token: str = Depends(oauth2_scheme)):
  try:
    payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
    return payload
  except jwt.PyJWTError:
    raise HTTPException(status_code=403, detail="Invalid authentication credentials")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(verify_jwt)):
  await websocket.accept()
  try:
    while True:
      data = await websocket.receive_text()
      await websocket.send_text(f"Message text was: {data}")
  except Exception as e:
    await websocket.close()


if __name__ == "__main__":
    uvicorn.run("main16_3:app", host="127.0.0.1", reload=True)