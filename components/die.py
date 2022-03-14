"""Tests for the Die component class"""
import random
from arcade import Sprite, load_spritesheet

from abstracts.colours import Colour, Colours
from abstracts.coords import Coords


class Die(Sprite):
    """Class for die component"""

    def __init__(
        self, center: Coords, colour: Colour = Colours.SKY.value, **sprite_kwargs
    ):

        super().__init__(
            image_width=64,
            image_height=64,
            center_x=center.x_coord,
            center_y=center.y_coord,
            **sprite_kwargs
        )

        self.color = colour
        self.side = 0
        self.rolling = True
        self.timer = 0

        self.textures = load_spritesheet(
            "images/dice_sprite_sheet.png",
            sprite_width=64,
            sprite_height=64,
            columns=6,
            count=6,
        )
        self.texture = self.textures[self.side]

    def update_animation(self, delta_time: float = 1 / 60):
        super().update_animation(delta_time)
        if self.rolling:
            self.timer += delta_time
            if self.timer > 0.15:
                self.timer = 0
                new_side = random.randrange(5)
                if new_side >= self.side:
                    new_side += 1
                self.side = new_side
                self.texture = self.textures[self.side]
