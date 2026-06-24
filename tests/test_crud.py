from src.database import SessionLocal, Base, engine
from src import crud

Base.metadata.create_all(bind=engine)


def test_create_task():
    db = SessionLocal()
    task = crud.create_task(db, "task 1")
    assert task.id is not None
    db.close()


def test_get_task():
    db = SessionLocal()
    task = crud.create_task(db, "task 2")

    found = crud.get_task(db, task.id)
    assert found is not None
    assert found.id == task.id
    db.close()


def test_update_task():
    db = SessionLocal()
    task = crud.create_task(db, "old")

    updated = crud.update_task(db, task.id, title="new", is_done=True)

    assert updated.title == "new"
    assert updated.is_done is True
    db.close()


def test_delete_task():
    db = SessionLocal()
    task = crud.create_task(db, "delete")

    deleted = crud.delete_task(db, task.id)
    found = crud.get_task(db, task.id)

    assert deleted.id == task.id
    assert found is None
    db.close()