from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    #
    # @validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
    #     if isinstance(v, str) and not v.startswith("["):
    #         return [i.strip() for i in v.split(",")]
    #     elif isinstance(v, (list, str)):
    #         return v
    #     raise ValueError(v)

    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_CLUSTER: str
    MONGO_DB: str
    MONGO_COLLECTION: str
    MONGO_URI: str = None

    @validator("MONGO_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return f'mongodb+srv://{values["MONGO_USERNAME"]}:{values["MONGO_PASSWORD"]}@{values["MONGO_CLUSTER"]}.aezmv.mongodb.net/{values["MONGO_DB"]}?retryWrites=true&w=majority'

    class Config:
        case_sensitive = True
        env_file = "../..env"


settings = Settings()
