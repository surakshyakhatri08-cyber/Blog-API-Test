import json
import os

DB_FILE = "db.json"

def _read_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def _write_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=2)


async def get_all_users():
    return _read_db()


async def get_user_by_id(user_id: int):
    data = _read_db()
    return next((user for user in data if user["id"] == user_id), None)


async def create_user(payload):
    data = _read_db()
    new_user = payload.model_dump()
    new_user["id"] = data[-1]["id"] + 1 if data else 1

    data.append(new_user)
    _write_db(data)
    return new_user


async def replace_user_logic(user_id: int, payload):
    data = _read_db()
    for user in data:
        if user["id"] == user_id:
            updated_data = payload.model_dump()
            updated_data["id"] = user_id
            user.update(updated_data)
            _write_db(data)
            return user
    return None


async def update_user_logic(user_id: int, payload):
    data = _read_db()
    for user in data:
        if user["id"] == user_id:
            update_data = payload.model_dump(exclude_unset=True)
            user.update(update_data)
            _write_db(data)
            return user
    return None


async def delete_user_logic(user_id: int):
    data = _read_db()
    user_index = next((i for i, user in enumerate(data) if user["id"] == user_id), None)

    if user_index is not None:
        deleted_user = data.pop(user_index)
        _write_db(data)
        return deleted_user
    return None