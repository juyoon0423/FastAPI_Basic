from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic 모델 정의
class Item(BaseModel):
    name: str
    price: float

# GET 요청
@app.get("/")
def read_root():
    return {"message": "Hello FastAPI!"}

# POST 요청
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
