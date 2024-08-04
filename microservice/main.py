
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from support.json_handler import JSONHandler
import os

app = FastAPI()

class RoutesMain:
    BASE_URL = "http://127.0.0.1:8000"
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    DATA = os.path.join(ROOT_PATH, "dataset", "data.json")


# Пример данных о пользователях
users_info = JSONHandler.load_json(RoutesMain.DATA)

# Модель данных для пользователя
class User(BaseModel):
    id: int
    name: str
    email: str

# Модель данных для создания пользователя
class UserCreate(BaseModel):
    name: str
    email: str

# Получить всех пользователей
@app.get("/users", response_model=List[User])
async def get_users():
    return users_info

# Получить пользователя по ID
@app.get("/user/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in users_info:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Создать нового пользователя
@app.post("/users", response_model=User)
async def create_user(user: UserCreate):
    users_info = JSONHandler.load_json(RoutesMain.DATA)
    new_user = {
        "id": len(users_info) + 1,
        "name": user.name,
        "email": user.email
    }
    users_info.append(new_user)
    JSONHandler.dump_json(RoutesMain.DATA, users_info)
    return new_user


# TODO
# Обновить информацию о пользователе
# Удалить пользователя
