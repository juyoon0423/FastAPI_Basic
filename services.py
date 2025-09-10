from sqlalchemy.orm import Session
from schemas import UserCreate
import crud
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(db: Session, user: UserCreate):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise ValueError("이미 등록된 이메일입니다.")

    hashed_pw = hash_password(user.password)
    return crud.create_user(db, user, hashed_pw)


def list_users(db: Session, skip: int = 0, limit: int = 10):
    return crud.get_users(db, skip=skip, limit=limit)
