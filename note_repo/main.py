from fastapi import FastAPI

from note_repo.dependencies import lifespan

from note_repo.routes import author, note

app = FastAPI(lifespan=lifespan)

app.include_router(author.router, prefix="/api")
app.include_router(note.router, prefix="/api")
