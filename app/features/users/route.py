from fastapi import APIRouter, HTTPException, status

from app.features.users.schema import CreateUserRequest, UpdateUserRequest
from app.features.users.service import (
    get_all_users,
    get_user_by_id,
    create_user,
    replace_user_logic,
    update_user_logic,
    delete_user_logic
)

router = APIRouter()

@router.get("")
async def get_users_details():
    return await get_all_users()

@router.get("/{user_id}")
async def get_user_detail(user_id: int):
    user = await get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} does not exist"
        )
    return user

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user_route(payload: CreateUserRequest):
    new_user = await create_user(payload)
    return {
        "message": "User created successfully",
        "user": new_user,
    }

@router.put("/{user_id}")
async def update_user(user_id: int, payload: CreateUserRequest):
    user = await replace_user_logic(user_id, payload)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} does not exist"
        )
    return {
        "message": "User PUT successfully",
        "user": user
    }

@router.patch("/{user_id}")
async def patch_user(user_id: int, payload: UpdateUserRequest):
    user = await update_user_logic(user_id, payload)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} does not exist"
        )
    return {
        "message": "User patched successfully",
        "user": user
    }

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    deleted_user = await delete_user_logic(user_id)
    if deleted_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} does not exist"
        )
    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }