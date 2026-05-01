from database.db import fetch_all, fetch_one, execute_query
from database.models import Recipe


class RecipeService:

    @staticmethod
    def get_all_recipes():
        rows = fetch_all("SELECT * FROM recipes")

        return [Recipe.from_db_row(row) for row in rows]

    @staticmethod
    def search_recipes(ingredients="", category=""):

        query = "SELECT * FROM recipes WHERE 1=1"
        params = []

        if category:
            query += " AND LOWER(category)=?"
            params.append(category.lower())

        rows = fetch_all(query, tuple(params))

        recipes = [Recipe.from_db_row(row) for row in rows]

        if ingredients:
            user_items = [
                item.strip().lower()
                for item in ingredients.split(",")
            ]

            filtered = []

            for recipe in recipes:
                recipe_ingredients = recipe.ingredients.lower().split(",")

                if any(
                    item in recipe_ingredients
                    for item in user_items
                ):
                    filtered.append(recipe)

            return filtered

        return recipes

    @staticmethod
    def get_recipe_by_name(name):

        row = fetch_one(
            "SELECT * FROM recipes WHERE LOWER(name)=?",
            (name.lower(),)
        )

        if row:
            return Recipe.from_db_row(row)

        return None

    @staticmethod
    def create_recipe(
        name,
        ingredients,
        steps,
        image,
        category
    ):

        execute_query(
            """
            INSERT INTO recipes
            (name, ingredients, steps, image, category)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                name,
                ingredients,
                steps,
                image,
                category
            )
        )