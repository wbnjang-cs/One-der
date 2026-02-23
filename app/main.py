from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import datetime
from uuid import uuid4

app = FastAPI()
class Event(BaseModel):
    name: str = "myEvent"
    year: int
    month: int
    day: int
    is_done: bool = False

    def __str__(self):
        return f"{self.name} is scheduled for {self.year}/{self.month}/{self.day}."

events = {}

@app.get("/")
def get_events():
    return events

@app.post("/events")
def create_event(event: Event):
    events[str(uuid4())] = event
    if(event.month > 12 or event.month < 1):
        raise HTTPException(status_code=406, detail = "Entered month is invalid")
    if(event.day > 32 or event.day < 1):
        raise HTTPException(status_code=406, detail = "Entered day is invalid")
        

    return {"message" : f"{event}, "}
    
