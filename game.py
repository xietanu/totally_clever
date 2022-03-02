"""
Main game class.
"""
import arcade

from components.markable_box import MarkableBox
from abstracts.multi_sprite_list import MultiSpriteList

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Totally Clever"

SCALING = 1


class TotallyClever(arcade.Window):
    """
    Totally Clever game class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.boxes = None
        self.box_texts = None
        self.marks = None

        arcade.set_background_color((0, 30, 50))

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.boxes = MultiSpriteList(use_spatial_hash=True)

        # This shows using a loop to place multiple sprites horizontally
        for x_coord in range(0, 400, 32):
            box = MarkableBox(x_coord + 16, 586, str(round(x_coord / 10)))
            self.boxes.append(box)

    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here
        self.boxes.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the user presses a mouse button."""
        boxes = arcade.get_sprites_at_point((x, y), self.boxes)

        if len(boxes) > 0:
            boxes[0].mark_box()

    # def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    #     """Called when the user presses a mouse button."""
    #     pass

    # def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    #     """User moves mouse"""
    #     pass
