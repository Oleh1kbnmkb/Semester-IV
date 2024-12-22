from fastapi import FastAPI, HTTPException
import requests  # Імпорт бібліотеки requests для HTTP-запитів
import uvicorn

app = FastAPI()

API_KEY = 'bddebc304257efa7289dcdb93bebeee5'

def get_weather_from_api(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ua"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"{weather_description.capitalize()}, {temperature}°C"
    else:
        return None

@app.get("/weather/{city}")
def get_weather(city: str):
    weather_info = get_weather_from_api(city)

    if weather_info:
        return {"city": city, "weather": weather_info}
    else:
        raise HTTPException(status_code=404, detail="Місто не знайдено або неможливо отримати дані")

if __name__ == "__main__":
    uvicorn.run("main4_7:app", host="127.0.0.1", reload=True)
