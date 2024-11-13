from fastapi.routing import APIRouter
from note_repo.schemas import db
from note_repo.dependencies import SessionDep
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.post("notes/")
def create_note(note: db.Note, session: SessionDep):
    session.add(note)
    session.commit()
    session.refresh(note)
    return note


@router.get("/api/notes/by-id/{note_id}", response_class=HTMLResponse)
def get_note(note_id: int, session: SessionDep):
    note = session.get(db.Note, note_id)
    return HTMLResponse(content=note.content)
