
from typing import Any, List, Optional
from pydantic import BaseModel
import uuid

# Временный Database класс для теста без реального MongoDB
class Database:
    def __init__(self, model):
        self.model = model
        self.data = {}  # имитируем базу данных в памяти
    
    # CREATE - создание записи
    async def save(self, document) -> None:
        doc_id = str(uuid.uuid4())
        document.id = doc_id  # добавляем ID документу
        self.data[doc_id] = document
        return
    
    # READ - получение одной записи по ID
    async def get(self, id: str) -> Any:
        return self.data.get(id, False)
    
    # READ ALL - получение всех записей
    async def get_all(self) -> List[Any]:
        return list(self.data.values())
    
    # UPDATE - обновление записи
    async def update(self, id: str, body: BaseModel) -> Any:
        if id not in self.data:
            return False
        
        doc = self.data[id]
        update_data = body.dict(exclude_unset=True)
        
        for key, value in update_data.items():
            setattr(doc, key, value)
        
        self.data[id] = doc
        return doc
    
    # DELETE - удаление записи
    async def delete(self, id: str) -> bool:
        if id not in self.data:
            return False
        del self.data[id]
        return True

# Заглушка для инициализации базы данных
async def init_db():
    print("✅ База данных инициализирована (работаем в режиме заглушки)")
    return
