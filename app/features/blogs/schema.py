from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional

class CreateBlog(BaseModel):
    title: str
    content: str
    is_published: bool = False

class UpdateBlog(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_published: Optional[bool] = None

class BlogResponse(BaseModel):
    id: UUID
    title: str
    content: str
    is_published: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class MessageResponse(BaseModel):
    message: str