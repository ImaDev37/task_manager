from fastapi import HTTPException


def validate_title(title: str):
    if not title or len(title.strip()) < 3:
        raise HTTPException(status_code=400, detail="Invalid title")
    return title.strip()


def validate_status(is_done: bool):
    if not isinstance(is_done, bool):
        raise HTTPException(status_code=400, detail="Invalid status")
    return is_done