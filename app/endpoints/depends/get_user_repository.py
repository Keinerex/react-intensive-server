from app.db import database
from app.repositories import Users as UsersRepository


def get_user_repository() -> UsersRepository:
    return UsersRepository(database)
