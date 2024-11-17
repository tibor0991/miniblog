from fastapi.routing import APIRouter
from note_repo.schemas import db
from note_repo.dependencies import SessionDep
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from sqlmodel import select
from jinja2 import PackageLoader, Environment



template = Jinja2Templates(env=Environment(
    loader=PackageLoader('note_repo')
))

from markdown import markdown

router = APIRouter()

@router.get("/blog/{note_id}", response_class=HTMLResponse)
def get_rendered_note(request: Request, note_id: int, session: SessionDep):
    statement = select(db.Note, db.Author).where(db.Note.note_id == note_id).join(db.Author)

    note, author = session.exec(statement).first()

    return template.TemplateResponse(
        request=request,
        name="page.html.jinja2",
        context={
            'title': note.title,
            'content': markdown(note.content),
            'author_name': markdown(f'_Author: {author.name} {author.surname}_')
        }
    )
