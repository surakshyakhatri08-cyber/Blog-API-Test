# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import declarative_base
# from app.core.config import settings
#
# engine = create_async_engine(settings.DATABASE_URL, echo=False)
#
# AsyncSessionLocal = async_sessionmaker(
#     bind=engine,
#     class_ = AsyncSession,
#     expire_on_commit = False,
#     autocommit = False
# )
#
# async def get_db():
#     async with AsyncSessionLocal() as session:
#         try:
#             yield session
#         finally:
#             await session.close()



import json
import os

DATA_FILE = "data.json"

def get_json_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)