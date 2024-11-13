from sqlmodel import SQLModel, Field
from datetime import datetime, date


class Author(SQLModel, table=True):
    __tablename__ = "authors"
    author_id: int = Field(primary_key=True)
    name: str
    surname: str
    date_of_birth: date


class Note(SQLModel, table=True):
    __tablename__ = "notes"
    note_id: int = Field(primary_key=True)
    author_id: int
    title: str
    content: str
    creation_date: datetime
    last_update: datetime
