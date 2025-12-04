from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])
user_database = Database(User)

# Временное хранилище пользователей
users_store = {}

# Регистрация пользователя
@user_router.post("/signup")
async def sign_user_up(user: User) -> dict:
    # Проверяем существует ли пользователь
    for existing_user in users_store.values():
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with email provided exists already."
            )
    
    # Сохраняем пользователя
    import uuid
    user.id = str(uuid.uuid4())
    users_store[user.id] = user
    
    return {
        "message": "User created successfully"
    }

# Вход пользователя
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    # Ищем пользователя
    for existing_user in users_store.values():
        if existing_user.email == user.email:
            if existing_user.password == user.password:
                return {
                    "message": "User signed in successfully."
                }
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid details passed."
                )
    
    # Если не нашли
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User with email does not exist."
    )
