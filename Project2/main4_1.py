from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()


weather_data = {
    "Київ": "Ясно, +20°C",
    "Львів": "Хмарно, +18°C",
    "Одеса": "Дощ, +22°C"
}

@app.get("/weather/{city}")
def get_weather(city: str):
    if city in weather_data:
        return {"city": city, "weather": weather_data[city]}
    else:
        raise HTTPException(status_code=404, detail="Місто не знайдено")



if __name__ == "__main__":
  uvicorn.run("main4_1:app", host="127.0.0.1", reload=True)