from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import date
import uvicorn

app = FastAPI()


class Event(BaseModel):
    id: int
    name: str
    date: date


events = []


@app.post("/events", response_model=Event, status_code=201)
def create_event(event: Event):
    if any(e.id == event.id for e in events):
        raise HTTPException(status_code=400, detail="Event with this ID already exists.")
    events.append(event)
    return event


@app.get("/events", response_model=List[Event])
def get_events():
    if not events:
        raise HTTPException(status_code=204)
    return events


@app.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int):
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    return event


@app.put("/events/{event_id}", response_model=Event)
def update_event(event_id: int, event_data: Event):
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    event.name = event_data.name
    event.date = event_data.date
    return event


@app.delete("/events/{event_id}", status_code=200)
def delete_event(event_id: int):
    global events
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    events = [e for e in events if e.id != event_id]
    return {"message": "Event deleted."}


@app.patch("/events/{event_id}/reschedule", response_model=Event)
def reschedule_event(event_id: int, new_date: date):
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    if new_date < date.today():
        raise HTTPException(status_code=400, detail="Date is invalid or in the past.")
    event.date = new_date
    return event


@app.post("/events/{event_id}/rsvp", status_code=200)
def rsvp_event(event_id: int):
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    return {"message": "RSVP successful!"}



if __name__ == "__main__":
  uvicorn.run("main7_3home:app", host="127.0.0.1", reload=True)