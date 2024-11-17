from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from note_repo.schemas.settings import AppSettings
from functools import lru_cache


@lru_cache
def get_settings():
    return AppSettings()

def create_engine_with_settings():
    settings = get_settings()
    return create_engine(str(settings.database_url))


db_engine = create_engine_with_settings()


def get_session():
    with Session(db_engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(db_engine)
    yield
