"""
Plugin for "https://orthrusonline.ru".
"""

from .plugin import Plugin


class OrthrusPlugin(Plugin, aliases=["orthrus"]):
    """
    Plugin for https://orthrusonline.ru - a pokemon game where you can get
    a reward every day just by logging into the game.
    """

    def __init__(self, **kwargs):
        print("Generated")

    def is_ready(self) -> bool:
        print("Checking")

    def run(self):
        print("Running")
