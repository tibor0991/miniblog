from fastapi.routing import APIRouter
from note_repo.schemas import db
from note_repo.dependencies import SessionDep

router = APIRouter()


@router.post("/api/authors/")
def create_author(author: db.Author, session: SessionDep):
    session.add(author)
    session.commit()
    session.refresh(author)
    return author
