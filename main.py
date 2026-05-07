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