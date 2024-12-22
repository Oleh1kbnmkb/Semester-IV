from fastapi import FastAPI, Path, Query, Header
from datetime import datetime
from typing import Optional
import uvicorn


app = FastAPI()


@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(..., title="User ID", description="The ID of the user", gt=0),
    timestamp: Optional[str] = Query(None, title="Timestamp", description="The timestamp of the request"),
    x_client_version: str = Header(..., alias="X-Client-Version")
):
    if not timestamp:
        timestamp = datetime.now().isoformat()

    return {
        "user_id": user_id,
        "timestamp": timestamp,
        "X-Client-Version": x_client_version,
        "message": f"Hello, user {user_id}!"
    }



if __name__ == "__main__":
  uvicorn.run("main5_home:app", host="127.0.0.1", reload=True)