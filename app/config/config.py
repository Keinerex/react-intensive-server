from os import environ
from pydantic import BaseSettings


class DefaultSettings(BaseSettings):

    PATH_PREFIX: str = environ.get("PATH_PREFIX", "")
    APP_HOST: str = environ.get("APP_HOST", "127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 8000))

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return "../base.db"
