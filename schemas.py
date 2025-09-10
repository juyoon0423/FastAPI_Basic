from pydantic import BaseModel, EmailStr

class ItemBase(BaseModel):
    name: str
    price: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True  # ORM 객체를 Pydantic 모델로 변환

# 회원가입 요청
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# 회원조회 응답
class User(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
