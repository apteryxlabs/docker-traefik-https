from motor.motor_asyncio import AsyncIOMotorCollection
from app.core.config import settings


async def _get_collection() -> AsyncIOMotorCollection:
    from app.main import MONGO_CLIENT
    col = MONGO_CLIENT.get_database(settings.MONGO_DB).get_collection(settings.MONGO_COLLECTION)
    return col


async def add_message(data):
    col = await _get_collection()
    result = await col.insert_one(data)
    if result.acknowledged:
        return True
    return False

async def get_messages():
    col = await _get_collection()
    messages = []
    async for result in col.find({}):
        result['_id'] = str(result['_id'])
        messages.append(result)
    return messages

