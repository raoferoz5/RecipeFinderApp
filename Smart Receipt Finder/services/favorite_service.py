from database.db import execute_query, fetch_all
from database.models import Recipe


class FavoriteService:

    @staticmethod
    def add_to_favorites(recipe_name):

        execute_query(
            "UPDATE recipes SET favorite=1 WHERE name=?",
            (recipe_name,)
        )

    @staticmethod
    def remove_from_favorites(recipe_name):

        execute_query(
            "UPDATE recipes SET favorite=0 WHERE name=?",
            (recipe_name,)
        )

    @staticmethod
    def get_favorites():

        rows = fetch_all(
            "SELECT * FROM recipes WHERE favorite=1"
        )

        return [Recipe.from_db_row(row) for row in rows]