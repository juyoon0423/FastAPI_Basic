from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import services, schemas
from database import SessionLocal

router = APIRouter(prefix="/users", tags=["users"])

# DB 세션 주입
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return services.register_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return services.list_users(db, skip=skip, limit=limit)
