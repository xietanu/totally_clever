"""Tests for the Die component class"""
from dataclasses import dataclass
import enum
import random
import arcade

import colours
import components
import sprites


@dataclass
class DieMode:
    """Defines die behaviour in a given state"""

    rolling: bool = False
    highlighted: bool = False


class DieModes(enum.Enum):
    """Enumates the possible dice states"""

    BASE = DieMode()
    ROLLING = DieMode(rolling=True)
    SELECTED = DieMode(highlighted=True)


class Die(sprites.MultiSprite):
    """Class for die component"""

    def __init__(
        self,
        center: components.Coords,
        colour: tuple[int, int, int] = colours.Category.SKY.value,
        **sprite_kwargs
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
        self.timer = 0

        self.mode = DieModes.ROLLING

        self.textures = arcade.load_spritesheet(
            "images/dice_sprite_sheet.png",
            sprite_width=64,
            sprite_height=64,
            columns=6,
            count=6,
        )
        self.texture = self.textures[self.side]

        self.selected_sprite = arcade.Sprite(
            "images/dice_highlight.png", center_x=self.center_x, center_y=self.center_y
        )

    def update_animation(self, delta_time: float = 1 / 60):
        """Updates the dice's visuals while rolling"""
        super().update_animation(delta_time)
        if self.mode == DieModes.ROLLING:
            self.timer += delta_time
            if self.timer > 0.15:
                self.timer = 0
                new_side = random.randrange(5)
                if new_side >= self.side:
                    new_side += 1
                self._set_side(new_side)

    def on_mouse_press(self):
        """Defines behaviour when clicked on"""
        if self.mode in [DieModes.BASE]:
            self.mode = DieModes.SELECTED
            self.sub_sprites.append(self.selected_sprite)
        elif self.mode == DieModes.SELECTED:
            self.reset_selection()

    def reset_selection(self):
        """Reset whether the die is selected"""
        self.mode = DieModes.BASE
        self.selected_sprite.remove_from_sprite_lists()

    def roll(self) -> None:
        """
        Randomise the side of the die
        """
        self._set_side(random.randrange(6))
        self.mode = DieModes.BASE

    def _set_side(self, value: int) -> None:
        """
        Set the side of the die to the specified value

        Args:
            value (int): value on the die
        """

        self.side = value - 1
        self.texture = self.textures[self.side]
