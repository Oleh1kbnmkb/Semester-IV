from fastapi import FastAPI, Path, Query
import uvicorn

app = FastAPI()

@app.get("/astronauts/{astronaut_id}")
async def get_astronaut(
    astronaut_id: int = Path(..., title="The ID of the astronaut to get information about"),
    detailed: bool = Query(False, description="Whether to return detailed information")
):
    astronaut_data = fetch_astronaut_data(astronaut_id, detailed)
    if astronaut_data:
        return astronaut_data
    return {"error": "Astronaut not found"}

def fetch_astronaut_data(astronaut_id, detailed):
    sample_astronauts = [
        {"id": 1, "name": "Yuri Gagarin", "missions": ["Vostok 1"]},
        {"id": 2, "name": "Someone", "missions": ["Space-X 1"]},
    ]
    astronaut = next((a for a in sample_astronauts if a["id"] == astronaut_id), None)
    if astronaut and detailed:
        astronaut["bio"] = "Some detailed biography..."
    return astronaut


if __name__ == "__main__":
  uvicorn.run("main5_7:app", host="127.0.0.1", reload=True)