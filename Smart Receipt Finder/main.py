from kivymd.app import MDApp
from kivy.lang import Builder

from database.db import init_db

from screens.main_screen import MainScreen
from screens.detail_screen import DetailScreen
from screens.favorite_screen import FavoriteScreen


class RecipeApp(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Blue"

        self.theme_cls.theme_style = "Dark"

        init_db()

        Builder.load_file("ui/detail.kv")
        Builder.load_file("ui/favorite.kv")

        return Builder.load_file("ui/main.kv")

    def toggle_theme(self):

        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"

        else:
            self.theme_cls.theme_style = "Dark"


RecipeApp().run()