from fastapi import FastAPI, WebSocket
import uvicorn

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    await websocket.send_text(f"Message text was: {data}")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  try:
    while True:
      data = await websocket.receive_text()
      print(data)
      await websocket.send_text(f"Повідомлення: {data}")
  except Exception as e:
    print(f"Помилка: {e}")
  finally:
    await websocket.close()


if __name__ == "__main__":
    uvicorn.run("main16_1:app", host="127.0.0.1", reload=True)