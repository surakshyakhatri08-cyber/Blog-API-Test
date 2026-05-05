from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .schema import CreateUserRequest, UpdateUserRequest
from . import service

router = APIRouter()

@router.get("/")
def get_users_details():
    return service.get_all_users()

@router.get("/{user_id}")
def get_user_detail(user_id: int):
    user = service.get_user_by_id(user_id)
    if user is None:
        return JSONResponse(status_code=404, content={"message": f"User with id {user_id} does not exist"})
    return user

@router.post("/")
def create_user(payload: CreateUserRequest):
    new_user = service.create_user(payload)
    return {
        "message": "User created successfully",
        "user": new_user,
    }


@router.put("/{user_id}")
def update_user(user_id: int,
                payload: CreateUserRequest):
    user = service.replace_user_logic(user_id, payload)

    if user is None:
        return JSONResponse(
            status_code=404,
            content={"message": f"User with id {user_id} does not exist"}
        )

    return {
        "message": "User PUT successfully",
        "user": user
    }

@router.patch("/{user_id}")
def patch_user(user_id: int, payload: UpdateUserRequest):
    user = service.update_user_logic(user_id, payload)
    if user is None:
        return JSONResponse(status_code=404, content={"message": f"User with id {user_id} does not exist"})
    return {
        "message": "User patched successfully",
        "user": user
    }

@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted_user = service.delete_user_logic(user_id)
    if deleted_user is None:
        return JSONResponse(status_code=404, content={"message": f"User with id {user_id} does not exist"})
    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }