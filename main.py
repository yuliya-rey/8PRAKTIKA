from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import init_db
from routes.events import event_router
from routes.users import user_router

import uvicorn

app = FastAPI()

# Регистрация маршрутов
app.include_router(event_router, prefix="/event")
app.include_router(user_router, prefix="/user")

@app.on_event("startup")
async def on_startup():
    """Инициализация при запуске"""
    try:
        await init_db()
        print("✅ База данных инициализирована")
    except Exception as e:
        print(f"⚠️  Ошибка инициализации БД: {e}")
        print("⚠️  Работаем в режиме заглушки")

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

@app.get("/test")
async def test():
    return {"message": "MongoDB server is working!"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
