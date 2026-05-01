from kivymd.uix.screen import MDScreen

from services.favorite_service import FavoriteService

from utils.helpers import show_message


class DetailScreen(MDScreen):

    current_recipe = None

    def load_recipe(self, recipe):

        self.current_recipe = recipe

        self.ids.recipe_name.text = recipe.name

        self.ids.recipe_ingredients.text = (
            f"Ingredients: {recipe.ingredients}"
        )

        self.ids.recipe_steps.text = (
            f"Steps: {recipe.steps}"
        )

        self.ids.recipe_image.source = recipe.image

    def toggle_favorite(self):

        if self.current_recipe.favorite == 1:

            FavoriteService.remove_from_favorites(
                self.current_recipe.name
            )

            self.current_recipe.favorite = 0

            show_message("Removed from favorites")

        else:

            FavoriteService.add_to_favorites(
                self.current_recipe.name
            )

            self.current_recipe.favorite = 1

            show_message("Added to favorites")