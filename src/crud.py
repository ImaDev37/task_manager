from sqlalchemy.orm import Session
from .models import Task
from .validators import validate_title, validate_status


def create_task(db: Session, title: str):
    task = Task(title=validate_title(title))
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_tasks(db: Session):
    return db.query(Task).all()


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: int, title: str = None, is_done: bool = None):
    task = get_task(db, task_id)

    if not task:
        return None

    if title is not None:
        task.title = validate_title(title)

    if is_done is not None:
        task.is_done = validate_status(is_done)

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)

    if not task:
        return None

    db.delete(task)
    db.commit()
    return task