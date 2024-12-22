from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections = []
    active_connections.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            logger.info
            if data == "ping":
                response = "pong"
            else:
                response = f"Отримано: {data}"
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Клієнт відключився")
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        await websocket.close()
        active_connections.remove(websocket)


if __name__ == "__main__":
    uvicorn.run("main16_2:app", host="127.0.0.1", reload=True)