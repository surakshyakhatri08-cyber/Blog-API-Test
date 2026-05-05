import json


DB_FILE = "db.json"


def get_all_users():
    with open(DB_FILE, "r") as file:
        data = json.load(file)
    return data


def get_user_by_id(user_id: int):
    with open(DB_FILE, "r") as file:
        data = json.load(file)
    user = next((user for user in data if user["id"] == user_id), None)
    return user


def create_user(payload):
    with open(DB_FILE, "r") as file:
        data = json.load(file)

    new_user = {
        "id": data[-1]["id"] + 1 if data else 1,
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "age": payload.age,
        "email": payload.email,
        "phone": payload.phone,
        "date_of_birth": payload.date_of_birth,
        "gender": payload.gender,
        "description": payload.description
    }

    data.append(new_user)
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=2)
    return new_user


def replace_user_logic(user_id: int, payload):
    with open(DB_FILE, "r") as file:
        data = json.load(file)

    user = next((user for user in data if user["id"] == user_id), None)

    if user is not None:
        user["first_name"] = payload.first_name
        user["last_name"] = payload.last_name
        user["age"] = payload.age
        user["email"] = payload.email
        user["phone"] = payload.phone
        user["date_of_birth"] = payload.date_of_birth
        user["gender"] = payload.gender
        user["description"] = payload.description

        with open(DB_FILE, "w") as file:
            json.dump(data, file, indent=2)

    return user


def update_user_logic(user_id: int, payload):
    with open(DB_FILE, "r") as file:
        data = json.load(file)

    user = next((user for user in data if user["id"] == user_id), None)
    if user is not None:
        if payload.first_name is not None: user["first_name"] = payload.first_name
        if payload.last_name is not None: user["last_name"] = payload.last_name
        if payload.age is not None: user["age"] = payload.age
        if payload.email is not None: user["email"] = payload.email
        if payload.phone is not None: user["phone"] = payload.phone
        if payload.date_of_birth is not None: user["date_of_birth"] = payload.date_of_birth
        if payload.gender is not None: user["gender"] = payload.gender
        if payload.description is not None: user["description"] = payload.description

        with open(DB_FILE, "w") as file:
            json.dump(data, file, indent=2)
    return user


def delete_user_logic(user_id: int):
    with open(DB_FILE, "r") as file:
        data = json.load(file)

    user_index = next((i for i, user in enumerate(data) if user["id"] == user_id), None)
    if user_index is not None:
        deleted_user = data.pop(user_index)
        with open(DB_FILE, "w") as file:
            json.dump(data, file, indent=2)
        return deleted_user
    return None