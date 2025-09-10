from sqlalchemy.orm import Session
from models import User, Item as ItemModel
from schemas import ItemCreate, UserCreate

# 아이템 생성
def create_item(db: Session, item: ItemCreate):
    db_item = ItemModel(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 모든 아이템 조회
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemModel).offset(skip).limit(limit).all()

# 특정 아이템 조회
def get_item(db: Session, item_id: int):
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate, hashed_password: str):
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()