from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.features.blogs.route import router as blog_router
app = FastAPI()

@app.get('/')
async def root():
    return RedirectResponse(url='/docs')
app.include_router(blog_router)