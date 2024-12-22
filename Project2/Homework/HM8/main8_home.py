from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime
import uvicorn

app = FastAPI()


movies_db = []


class Movie(BaseModel):
    id: int
    title: str
    director: str
    release_year: int = Field(..., gt=1888, le=datetime.now().year)
    rating: float = Field(..., ge=0.0, le=10.0)


    @validator("release_year")
    def check_release_year(cls, v):
        current_year = datetime.now().year
        if v > current_year:
            raise ValueError("Рік випуску не може бути у майбутньому.")
        return v

@app.get("/movies", response_model=List[Movie])
async def get_movies():
    return movies_db

@app.post("/movies", response_model=Movie)
async def add_movie(movie: Movie):
    for existing_movie in movies_db:
        if existing_movie.id == movie.id:
            raise HTTPException(status_code=400, detail="Фільм з таким ID вже існує.")
    movies_db.append(movie)
    return movie

@app.get("/movies/{id}", response_model=Movie)
async def get_movie(id: int):
    for movie in movies_db:
        if movie.id == id:
            return movie
    raise HTTPException(status_code=404, detail="Фільм не знайдено.")

@app.delete("/movies/{id}", response_model=Movie)
async def delete_movie(id: int):
    for index, movie in enumerate(movies_db):
        if movie.id == id:
            removed_movie = movies_db.pop(index)
            return removed_movie
    raise HTTPException(status_code=404, detail="Фільм не знайдено.")



if __name__ == "__main__":
  uvicorn.run("main8_home:app", host="127.0.0.1", reload=True)