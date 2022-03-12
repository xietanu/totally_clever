"""Tests for the Die component class"""
from abstracts.colours import Colour, Colours
from abstracts.coords import Coords
from arcade import Sprite


class Die(Sprite):
    """Class for die component"""

    def __init__(
        self, center: Coords, colour: Colour = Colours.SAPPHIRE.value, **sprite_kwargs
    ):

        super().__init__(
            filename="images/dice_sprite_sheet.png",
            image_width=64,
            image_height=64,
            center_x=center.x_coord,
            center_y=center.y_coord,
            **sprite_kwargs
        )

        self.colour = colour
