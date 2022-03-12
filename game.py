"""
Main game class.
"""
import arcade
from abstracts.colours import Colours

from abstracts.coords import Coords
from abstracts.multi_sprite_list import MultiSpriteList
from components.die import Die

from components.score_category import ScoreCategory, MarkPrereqMode


# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Totally Clever"

SCALING = 1

class TotallyClever(arcade.Window):
    """
    Totally Clever game class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.score_categories = None
        self.dice = None

        arcade.set_background_color((0, 30, 50))

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.score_categories = MultiSpriteList(use_spatial_hash=True)
        self.dice = arcade.SpriteList()

        green_category = ScoreCategory(
            "images/GreenCategoryBox.png",
            Coords(300,0),
            mark_prereq_mode=MarkPrereqMode.PREVIOUS,
        )
        self.score_categories.append(green_category)

        green_category.add_decorative_sprite("images/green_icon.png", Coords(30, 50))

        green_box_texts = [
            ">0",
            ">1",
            ">2",
            ">3",
            ">4",
            ">0",
            ">1",
            ">2",
            ">3",
            ">4",
            ">5",
        ]
        for x_offset, text in enumerate(green_box_texts):
            green_category.add_box(Coords(70 + 40 * x_offset, 50), text=text)

        self.dice.append(Die(Coords(64,64), colour=Colours.FLAME.value))

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.score_categories.draw()
        self.dice.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the user presses a mouse button."""
        categories = arcade.get_sprites_at_point((x, y), self.score_categories)

        if len(categories) > 0:
            categories[0].on_mouse_press(Coords(x, y))

    # def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    #     """Called when the user presses a mouse button."""
    #     pass

    # def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    #     """User moves mouse"""
    #     pass
