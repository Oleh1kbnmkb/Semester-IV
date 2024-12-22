from fastapi import FastAPI, APIRouter, Request
import uvicorn

router = APIRouter()

@router.get("/specific-route")
async def specific_route():
    return {"message": "Специфічний маршрут"}

app = FastAPI()

@app.middleware("http")
async def custom_middleware(request: Request, call_next):
    if request.url.path == "/specific-route":
        print("Middleware виконується для /specific-route")
    response = await call_next(request)
    return response

app.include_router(router)



if __name__ == "__main__":
  uvicorn.run("main13_4:app", host="127.0.0.1", reload=True)
