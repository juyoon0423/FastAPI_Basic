from sqlalchemy.orm import Session
from models import Item as ItemModel
from schemas import ItemCreate

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
