from motor.motor_asyncio import AsyncIOMotorCollection
from app.core.config import settings


async def _get_collection() -> AsyncIOMotorCollection:
    from app.main import MONGO_CLIENT
    col = MONGO_CLIENT.get_database(settings.MONGO_DB).get_collection(settings.MONGO_COLLECTION)
    return col


