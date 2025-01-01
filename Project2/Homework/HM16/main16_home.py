from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import List
from jose import JWTError, jwt
import asyncio
import uvicorn


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


fake_users_db = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"},
}


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{token}")
async def websocket_endpoint(websocket: WebSocket, token: str):
    try:
        username = decode_token(token)
    except HTTPException:
        await websocket.close(code=4001)
        return

    await manager.connect(websocket)
    await manager.broadcast(f"{username} joined the chat.")
    try:
        while True:
            data = await websocket.receive_text()
            sanitized_message = data.replace("<", "&lt;").replace(">", "&gt;")
            await manager.broadcast(f"{username}: {sanitized_message}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"{username} left the chat.")


@app.post("/token")
def generate_token(username: str):
    if username not in fake_users_db:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": username}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/status")
async def status():
    return {"status": "Chat server is running!"}


def test_chat_server():
    from fastapi.testclient import TestClient

    client = TestClient(app)

    response = client.post("/token", json={"username": "user1"})
    assert response.status_code == 200
    token = response.json()["access_token"]

    with client.websocket_connect(f"/ws/{token}") as websocket:
        websocket.send_text("Hello, World!")
        response = websocket.receive_text()
        assert "Hello, World!" in response



if __name__ == "__main__":
  uvicorn.run("main16_home:app", host="127.0.0.1", reload=True)
