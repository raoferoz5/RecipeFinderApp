from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget

from services.recipe_service import RecipeService


class MainScreen(MDScreen):

    def find_recipes(self):

        recipe_list = self.ids.recipe_list

        recipe_list.clear_widgets()

        ingredients = self.ids.ingredients_input.text

        category = self.ids.category_input.text

        recipes = RecipeService.search_recipes(
            ingredients,
            category
        )

        for recipe in recipes:

            item = TwoLineAvatarListItem(
                text=recipe.name,
                secondary_text=recipe.category
            )

            image = ImageLeftWidget(
                source=recipe.image
            )

            item.add_widget(image)

            item.bind(
                on_release=lambda x, r=recipe:
                self.open_recipe(r)
            )

            recipe_list.add_widget(item)

    def open_recipe(self, recipe):

        detail_screen = self.manager.get_screen("detail")

        detail_screen.load_recipe(recipe)

        self.manager.current = "detail"