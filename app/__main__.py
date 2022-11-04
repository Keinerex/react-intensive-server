import pprint

import uvicorn
from fastapi import FastAPI

from app.config import DefaultSettings
from app.config.utils import get_settings
from app.db import database
from app.endpoints import list_of_routes


def bind_routes(application: FastAPI, setting: DefaultSettings) -> None:
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    description = "Бэкенд для магазина книг"

    application = FastAPI(
        title="Book store",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
    )
    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()


@app.on_event("startup")
async def database_connect():
    database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    database.disconnect()


@app.get("/categories")
async def test():
    query = "select * from Categories"
    return database.fetch_all(query)


@app.get("/books")
async def test(category_id=""):
    query = f'select id, title, price, annotation, genre_id from Books where categories_id = "{category_id}"'
    response = []
    for id, title, price, annotation, genre_id in database.fetch_all(query):
        response.append({
            "id": id,
            "title": title,
            "price": price,
            "annotation": annotation,
            "genre": database.fetch_one(f'select genre from Genres where id = "{genre_id}"')[0],
            "authors": [i[0] for i in database.fetch_all(
                f'select name from Authors where id in (select author_id from AuthorBooks where book_id = "{id}")')]
        })
    return response


@app.get("/reviews")
async def test(book_id=""):
    query = f'select id, user_id, rate, text from Reviews where book_id = "{book_id}"'
    response = []
    for id, user_id, rate, text in database.fetch_all(query):
        response.append({
            "id": id,
            "rate": rate,
            "text": text,
            "user": database.fetch_one(f'select name from Users where id = "{user_id}"')[0],
        })
    pprint.pprint(response)
    return response


if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
