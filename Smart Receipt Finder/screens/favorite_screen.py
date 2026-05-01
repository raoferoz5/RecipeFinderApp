from kivymd.uix.screen import MDScreen

from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.list import ImageLeftWidget

from services.favorite_service import FavoriteService


class FavoriteScreen(MDScreen):

    def load_favorites(self):

        fav_list = self.ids.fav_list

        fav_list.clear_widgets()

        recipes = FavoriteService.get_favorites()

        for recipe in recipes:

            item = TwoLineAvatarListItem(
                text=recipe.name,
                secondary_text=recipe.category
            )

            image = ImageLeftWidget(
                source=recipe.image
            )

            item.add_widget(image)

            fav_list.add_widget(item)