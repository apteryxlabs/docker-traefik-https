from motor.motor_asyncio import AsyncIOMotorCollection
from {{ cookiecutter.pkg_name }}.core.config import settings


async def _get_collection() -> AsyncIOMotorCollection:
    from {{ cookiecutter.pkg_name }}.main import MONGO_CLIENT
    col = MONGO_CLIENT.get_database(settings.MONGO_DB).get_collection(settings.MONGO_COLLECTION)
    return col


