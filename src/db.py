from collections.abc import Generator
from typing import Any

from sqlmodel import Session, SQLModel, create_engine

engine = create_engine('sqlite:///database.db')


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
