from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.events import Event, EventUpdate
from typing import List

event_router = APIRouter(tags=["Events"])
event_database = Database(Event)

# CREATE - Создание события
@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Event created successfully"
    }

# READ ALL - Получение всех событий
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

# READ ONE - Получение события по ID
@event_router.get("/{id}")
async def retrieve_event(id: str) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event

# UPDATE - Обновление события
@event_router.put("/{id}")
async def update_event(id: str, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event

# DELETE - Удаление события
@event_router.delete("/{id}")
async def delete_event(id: str) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully."
    }
