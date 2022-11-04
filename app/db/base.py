import sqlite3
from sqlite3 import Connection
from typing import Optional, Iterable, Any


class Database:
    def __init__(self, url: str):
        self._url = url
        self._connection: Optional[Connection] = None

    def connect(self):
        self._connection: Connection = sqlite3.connect(self._url)

    def fetch_all(self, query, values: Iterable[Any] = None):
        if not self._connection:
            raise ConnectionError
        cur = self._connection.cursor()
        if values:
            res = list(cur.execute(query, values).fetchall())
        else:
            res = list(cur.execute(query).fetchall())
        cur.close()
        return res

    def fetch_one(self, query, values: Iterable[Any] = None):
        if not self._connection:
            raise ConnectionError
        cur = self._connection.cursor()
        if values:
            res = list(cur.execute(query, values).fetchone())
        else:
            res = list(cur.execute(query).fetchone())
        cur.close()
        return res

    def disconnect(self):
        self._connection.close()
