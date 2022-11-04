from app.config.utils import get_settings
from app.db.base import Database

settings = get_settings()

database = Database(settings.database_uri)

__all__ = [
    "database"
]
