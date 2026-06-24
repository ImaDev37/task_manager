from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"status": "ok"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks")
def create_task(title: str, db: Session = Depends(get_db)):
    return crud.create_task(db, title)


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    return crud.get_task(db, task_id)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str = None, is_done: bool = None, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, title, is_done)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)