from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: str = Header(None), x_token: str = Header(...)):
  if x_token != "secret-token":
    raise HTTPException(status_code=400, detail="X-Token header invalid")

  return {"User-Agent": user_agent, "X-Token": x_token}


@app.get("/data/")
async def get_data(
        x_custom_header: str = Header(None),
        authorization: str = Header(...)
):
  if authorization != "Bearer mysecrettoken":
    raise HTTPException(status_code=401, detail="Unauthorized")

  return {
    "message": "Success",
    "x_custom_header": x_custom_header
  }


@app.get("/info/")
async def get_info(accept: str = Header(default="application/json")):
  data = {"message": "This is a JSON response"}

  if "application/json" in accept:
    return JSONResponse(content=data)
  elif "text/html" in accept:
    html_content = "<html><body><h1>This is an HTML response</h1></body></html>"
    return HTMLResponse(content=html_content)
  else:
    raise HTTPException(status_code=406, detail="Not Acceptable")


@app.get("/user-agent/")
async def read_user_agent(user_agent: str = Header(None)):
  if user_agent:
    return {"User-Agent": user_agent}
  else:
    return {"message": "User-Agent header is missing"}

# To run the application, use the command: uvicorn <filename>:app --reload
if __name__ == "__main__":
  uvicorn.run("main5_9:app", host="127.0.0.1", reload=True)