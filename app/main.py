from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.database import add_message, get_messages


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


MONGO_CLIENT = AsyncIOMotorClient(settings.MONGO_URI)

@app.get('/')
async def hi():
    return {'hello': 'world'}

@app.get('/messages')
async def retrieve_messages():
    result = await get_messages()
    return result

@app.post('/messages')
async def post_message(message: dict = Body(...)):
    resp = await add_message(message)
    return resp

if __name__ == '__main__':
    import dotenv
    import uvicorn

    dotenv.load_dotenv('../.env.backend')
    uvicorn.run('app.main:app', host="0.0.0.0", port=80, reload=True)