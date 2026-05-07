from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID
from app.db.session import get_db
from app.features.blogs.service import BlogService
from app.features.blogs.schema import CreateBlog, UpdateBlog, BlogResponse, MessageResponse

router = APIRouter(tags=['Blogs'], prefix='/blogs')

def get_blog_service(db: AsyncSession = Depends(get_db)) -> BlogService:
    return BlogService(db)

@router.post('', response_model=BlogResponse, status_code=status.HTTP_201_CREATED)
async def create(payload: CreateBlog, blog_service: BlogService = Depends(get_blog_service)):
    return await blog_service.create_blog(payload)

@router.get('', response_model=List[BlogResponse])
async def list_blogs(blog_service: BlogService = Depends(get_blog_service)):
    blogs = await blog_service.get_all_blogs()
    if blogs is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blogs

@router.get('/{blog_id}', response_model=BlogResponse)
async def get_blog(blog_id: UUID, blog_service: BlogService = Depends(get_blog_service)):
    blog = await blog_service.get_blog_by_id(blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

@router.patch('/{blog_id}', response_model=BlogResponse)
async def update(blog_id: UUID, payload: UpdateBlog, blog_service: BlogService = Depends(get_blog_service)):
    updated_blog = await blog_service.update_blog(blog_id, payload)
    if updated_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated_blog

@router.delete('/{blog_id}', response_model=MessageResponse)
async def delete(blog_id: UUID, blog_service: BlogService = Depends(get_blog_service)):
    success = await blog_service.delete_blog(blog_id)
    if success is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Blog deleted successfully"}