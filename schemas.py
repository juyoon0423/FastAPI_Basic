from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True  # ORM 객체를 Pydantic 모델로 변환
