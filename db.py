import sqlite3
import os

DB_NAME = "recipes.db"

# ---------------- Initialize Database ----------------
def init_db():
    create_images_folder()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        ingredients TEXT,
        steps TEXT,
        image TEXT,
        category TEXT,
        favorite INTEGER DEFAULT 0
    )
    """)

    # Seed recipes if table empty
    cursor.execute("SELECT COUNT(*) FROM recipes")
    count = cursor.fetchone()[0]
    if count == 0:
        recipes = [
            ("Omelette", "egg,onion,salt", "Beat eggs and fry with onion", "images/omelette.jpg", "Breakfast"),
            ("Tomato Egg Curry", "egg,tomato,onion,spices", "Cook tomato and add eggs", "images/tomato_egg_curry.jpg", "Dinner")
        ]
        cursor.executemany(
            "INSERT INTO recipes (name, ingredients, steps, image, category) VALUES (?,?,?,?,?)",
            recipes
        )

    conn.commit()
    conn.close()

def create_images_folder():
    if not os.path.exists("images"):
        os.makedirs("images")


# ---------------- Fetch All Recipes ----------------
def get_recipes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, ingredients, category, image FROM recipes")
    rows = cursor.fetchall()
    conn.close()
    return rows


# ---------------- Get Recipe Details ----------------
def get_recipe_details(name):
    name = str(name).lower()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, ingredients, steps, image FROM recipes WHERE LOWER(name) = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    return row


# ---------------- Favorites ----------------
def add_favorite(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE recipes SET favorite = 1 WHERE name = ?", (name,))
    conn.commit()
    conn.close()


def remove_favorite(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE recipes SET favorite = 0 WHERE name = ?", (name,))
    conn.commit()
    conn.close()


def is_favorite(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT favorite FROM recipes WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0] == 1
    return False


def get_favorites():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT name, category, image FROM recipes WHERE favorite = 1")
    rows = cursor.fetchall()
    conn.close()
    return rows
