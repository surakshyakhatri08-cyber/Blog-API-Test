# from datetime import datetime
# from fastapi import FastAPI, Depends, HTTPException, status
# from pydantic import BaseModel
# from select import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.db.models import Todo
# from app.db.session import get_db
#
# app = FastAPI(title="NCMT API")
#
# class TodoCreate(BaseModel):
#     title: str
#     description: str
#     is_completed: bool = False
#
# class TodoResponse(BaseModel):
#     id: int
#     title: str
#     description: str
#     is_completed: bool
#     created_at: datetime
#     updated_at: datetime
#
#     class Config:
#         from_attributes = True
#
# @app.get("/", response_model=list[TodoResponse])
# async def root(db: AsyncSession = Depends(get_db)):
#     stmt = select(Todo)
#     result = await db.execute(stmt)
#
#     data = result.scalars().all()
#
#     if data is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Not Found")
#
#     return data
#
# @app.post("/todos", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
# async def create_todo(todo_in: TodoCreate, db: AsyncSession = Depends(get_db)):
#
#     new_todo = Todo(**todo_in.model_dump())
#
#     db.add(new_todo)
#     await db.commit()
#     await db.refresh(new_todo)
#
#     return new_todo

from fastapi import FastAPI
from app.features.users.route import router as user_router

app = FastAPI(
    title="NCMT API",
    description="Assignment: User Management System using db.json",
    version="1.0.0"
)
@app.get("/", tags=["General"])
async def root():
    return {
        "status": "Online",
        "message": "Welcome to NCMT API - User Management System"
    }

app.include_router(user_router, prefix="/users", tags=["Users"])