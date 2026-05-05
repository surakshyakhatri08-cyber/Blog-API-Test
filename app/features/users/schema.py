from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: EmailStr
    phone: str
    date_of_birth: str
    gender: Gender
    description: Optional[str] = None

class UpdateUserRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[Gender] = None
    description: Optional[str] = None