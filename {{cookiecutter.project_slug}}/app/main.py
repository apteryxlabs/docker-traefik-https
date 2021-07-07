from fastapi import FastAPI, Body

{% if cookiecutter.use_cors == 'YES' %}
from fastapi.middleware.cors import CORSMiddleware
{% endif %}

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings



def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    {% if cookiecutter.use_cors == 'YES' %}
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    {% endif %}

    return _app


app = get_application()

{% if cookiecutter.use_mongo == 'YES' %}

MONGO_CLIENT = AsyncIOMotorClient(settings.MONGO_URI)
{% endif %}

@app.get('/')
async def hi():
    return {'hello': 'world'}


if __name__ == '__main__':
    import dotenv
    import uvicorn

    dotenv.load_dotenv('../.env.backend')
    uvicorn.run('app.main:app', host="0.0.0.0", port=80, reload=True)