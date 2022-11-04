from app.repositories.base import BaseRepository
from app.models import User


class Users(BaseRepository):
    async def get_all(self) -> list[User]:
        query = "select * from users"
        return [
            User(
                id=obj[0],
                name=obj[1]
            ) for obj in self.database.fetch_all(query)
        ]
