from sqlalchemy.ext.asyncio import AsyncSession, result
from sqlalchemy.future import select
from sqlalchemy import update, delete
from uuid import UUID
from typing import Optional
from sqlalchemy import Sequence
from app.db.models import Blog
from app.features.blogs.schema import CreateBlog, UpdateBlog

class BlogService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_blog(self, payload: CreateBlog) -> Blog:
        new_blog = Blog(
            title=payload.title,
            content=payload.content,
            is_published=payload.is_published
        )
        self.db.add(new_blog)
        await self.db.commit()
        await self.db.refresh(new_blog)
        return new_blog

    async def get_all_blogs(self) -> Sequence[Blog]:
        query = select(Blog).order_by(Blog.created_at.desc())
        blog = await self.db.execute(query)
        return blog.scalars().all()

    async def get_blog_by_id(self, blog_id: UUID) -> Blog | None:
        query = select(Blog).where(Blog.id == blog_id)
        blog = await self.db.execute(query)
        return blog.scalars().first()

    async def update_blog(self, blog_id: UUID, payload: UpdateBlog) -> Optional[Blog] | None:
        blog = await self.get_blog_by_id(blog_id)

        update_data = payload.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(blog, key, value)

        await self.db.commit()
        await self.db.refresh(blog)
        return blog

    # async def update_blog(self, blog_id: UUID, payload: UpdateBlog) -> Blog:
    #     blog = await self.get_blog_by_id(blog_id)
    #     if not blog:
    #         return None
    #
    #     blog.title = payload.title
    #     blog.content = payload.content
    #     blog.is_published = payload.is_published
    #     return blog


    async def delete_blog(self, blog_id: UUID) -> bool | None:
        blog = await self.get_blog_by_id(blog_id)

        await self.db.delete(blog)
        await self.db.commit()

        return True