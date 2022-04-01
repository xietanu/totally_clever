"""
Main game class.
"""
import arcade

from abstracts.coords import Coords
from abstracts.multi_sprite_list import MultiSpriteList
from components.button import Button
from components.die import Die
from components.score_categories.at_least_category import AtLeastCategory
from components.score_categories.score_category import ScoreCategory
from visual_elements.colours import Colours
from visual_elements.standard_sprites import ScoreCategorySpriteFilepath


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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # type: ignore
        arcade.set_background_color((0, 30, 50))
        self.timer = 0

        self.score_categories = MultiSpriteList(use_spatial_hash=True)
        self.dice = MultiSpriteList()
        self.buttons = MultiSpriteList(use_spatial_hash=True)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.timer = 0

        self.score_categories = MultiSpriteList(use_spatial_hash=True)
        self.dice = MultiSpriteList()
        self.buttons = MultiSpriteList(use_spatial_hash=True)

        at_least_category = AtLeastCategory(
            ScoreCategorySpriteFilepath.SHORT.value,
            Colours.SUNGLOW.value,
            Coords(300, 0),
        )
        self.score_categories.append(at_least_category)

        at_least_category.add_decorative_sprite(
            "images/arrow_icon.png", Coords(30, 50), apply_color=True
        )

        at_least_box_texts = [
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
        for x_offset, text in enumerate(at_least_box_texts):
            at_least_category.add_box(Coords(70 + 40 * x_offset, 50), label=text)

        self.dice.append(Die(Coords(64, 64), colour=Colours.SKY.value))
        self.dice.append(Die(Coords(64, 128), colour=Colours.ALABASTER.value))
        self.dice.append(Die(Coords(64, 192), colour=Colours.SALMON.value))
        self.dice.append(Die(Coords(64, 256), colour=Colours.SUNGLOW.value))
        self.dice.append(Die(Coords(64, 318), colour=Colours.LIBERTY.value))

        self.buttons.append(
            Button(
                button_id="roll_dice",
                center=Coords(100, SCREEN_HEIGHT - 40),
                text="Roll!",
                colour=Colours.SKY.value,
            )
        )

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.score_categories.draw()
        self.dice.draw()
        self.buttons.draw()

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        for die in self.dice:
            die.update_animation()

    def on_mouse_press(self, x, y, button, modifiers):
        """Called when the user presses a mouse button."""
        categories = arcade.get_sprites_at_point((x, y), self.score_categories)
        dice = arcade.get_sprites_at_point((x, y), self.dice)

        if len(categories) > 0 and isinstance(categories[0], ScoreCategory):
            categories[0].on_mouse_press(Coords(int(x), int(y)))

        if len(dice) > 0 and isinstance(dice[0], Die):
            dice[0].on_mouse_press()
