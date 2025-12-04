from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):  # Убираем Document
    email: str
    password: str
    events: List[str] = []
    id: Optional[str] = None

class UserSignIn(BaseModel):
    email: str
    password: str
