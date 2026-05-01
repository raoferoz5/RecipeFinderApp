from kivymd.uix.snackbar import Snackbar


def show_message(text):
    Snackbar(
        text=text,
        duration=2
    ).open()