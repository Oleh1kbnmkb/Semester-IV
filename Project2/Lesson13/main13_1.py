from fastapi import FastAPI, Request
import time
import logging
import uvicorn

app = FastAPI()

logger = logging.getLogger("middleware_logger")
logging.basicConfig(level=logging.INFO)

async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    logger.info(f"Запит: {request.method} {request.url} - Затрачений час: {process_time}ms")
    return response
app.middleware("http")(log_requests)
@app.get("/")
async def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
  uvicorn.run("main13_1:app", host="127.0.0.1", reload=True)