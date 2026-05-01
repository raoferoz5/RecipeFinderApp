import sqlite3
from contextlib import closing

DB_NAME = "recipes.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            steps TEXT NOT NULL,
            image TEXT,
            category TEXT,
            favorite INTEGER DEFAULT 0
        )
        """)

        conn.commit()


def fetch_all(query, params=()):
    with closing(get_connection()) as conn:
        cursor = conn.execute(query, params)
        return cursor.fetchall()


def fetch_one(query, params=()):
    with closing(get_connection()) as conn:
        cursor = conn.execute(query, params)
        return cursor.fetchone()


def execute_query(query, params=()):
    with closing(get_connection()) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()