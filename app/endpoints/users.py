from fastapi import APIRouter, Depends

from app.endpoints.depends import get_user_repository
from app.models import User as UserModel
from app.repositories import Users as UsersRepository

api_router = APIRouter(tags=["User"])


@api_router.get(
    "/get_users",
    response_model=list[UserModel],
)
async def get_users(
        users_repository: UsersRepository = Depends(get_user_repository)
):
    return await users_repository.get_all()