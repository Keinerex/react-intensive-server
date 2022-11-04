from app.endpoints.users import api_router as users_router

list_of_routes = [
    users_router,
]

__all__ = [
    "list_of_routes"
]
