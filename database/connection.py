from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

# Настройки базы данных
database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}

# Создаём движок базы данных
engine_url = create_engine(
    database_connection_string,
    echo=True,
    connect_args=connect_args
)

def conn():
    """Создаёт все таблицы в базе данных"""
    SQLModel.metadata.create_all(engine_url)

def get_session():
    """Генератор сессий для зависимостей"""
    with Session(engine_url) as session:
        yield session
