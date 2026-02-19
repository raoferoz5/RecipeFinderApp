from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.button import MDIconButton
import db


class RecipeApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Orange"
        db.init_db()
        return Builder.load_file("ui.kv")

    # ---------------- Find Recipes ----------------
    def find_recipes(self):
        recipe_list = self.root.get_screen("main").ids.recipe_list
        recipe_list.clear_widgets()

        user_input = self.root.get_screen("main").ids.ingredients_input.text.lower().strip()
        category_input = self.root.get_screen("main").ids.category_input.text.lower().strip()

        recipes = db.get_recipes()
        matched_recipes = []

        if not user_input:
            for name, ingredients, category, image in recipes:
                if category_input and category.lower() != category_input:
                    continue
                matched_recipes.append((name, category, image))
        else:
            user_items = [i.strip() for i in user_input.split(",") if i.strip()]

            for name, ingredients, category, image in recipes:
                if category_input and category.lower() != category_input:
                    continue

                ingredients_list = ingredients.lower().split(",")
                if any(item in ingredients_list for item in user_items):
                    matched_recipes.append((name, category, image))

        for name, category, image in matched_recipes:
            item = TwoLineAvatarListItem(text=name, secondary_text=category)
            img = ImageLeftWidget(source=image)
            item.add_widget(img)

            # Open details
            item.bind(on_release=lambda x, n=name: self.open_details(n))

            recipe_list.add_widget(item)

    # ---------------- Open Recipe Details ----------------
    def open_details(self, recipe_name):
        details = db.get_recipe_details(recipe_name)
        if not details:
            return

        name, ingredients, steps, image = details
        screen = self.root.get_screen("detail")

        screen.ids.recipe_name.text = name
        screen.ids.recipe_ingredients.text = f"Ingredients: {ingredients}"
        screen.ids.recipe_steps.text = f"Steps: {steps}"
        screen.ids.recipe_image.source = image

        fav_btn = screen.ids.fav_button
        if db.is_favorite(name):
            fav_btn.text = "Remove from Favorites"
            fav_btn.text_color = (1, 0, 0, 1)
        else:
            fav_btn.text = "Add to Favorites"
            fav_btn.text_color = (0, 0, 0, 1)

        self.root.current = "detail"

    # ---------------- Toggle Favorite (Detail Screen) ----------------
    def toggle_favorite_detail(self):
        screen = self.root.get_screen("detail")
        name = screen.ids.recipe_name.text
        fav_btn = screen.ids.fav_button

        if db.is_favorite(name):
            db.remove_favorite(name)
            fav_btn.text = "Add to Favorites"
            fav_btn.text_color = (0, 0, 0, 1)
        else:
            db.add_favorite(name)
            fav_btn.text = "Remove from Favorites"
            fav_btn.text_color = (1, 0, 0, 1)

    # ---------------- Show Favorites ----------------
    def show_favorites(self):
        fav_screen = self.root.get_screen("favorite")
        fav_list = fav_screen.ids.fav_list
        fav_list.clear_widgets()

        favorites = db.get_favorites()  # (name, category, image)

        for name, category, image in favorites:
            item = TwoLineAvatarListItem(text=name, secondary_text=category)
            img = ImageLeftWidget(source=image)
            item.add_widget(img)
            item.bind(on_release=lambda x, n=name: self.open_details(n))
            fav_list.add_widget(item)

        self.root.current = "favorite"

    # ---------------- Navigation ----------------
    def go_back(self):
        self.root.current = "main"

    def go_back_from_fav(self):
        self.root.current = "main"


if __name__ == "__main__":
    RecipeApp().run()
