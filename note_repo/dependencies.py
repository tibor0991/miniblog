from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager


postgres_url = "postgresql+psycopg://tibor:diocan@localhost:5432/note_repo"

db_engine = create_engine(postgres_url)


def get_session():
    with Session(db_engine) as session:
        print("Called only once?")
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(db_engine)
    yield
