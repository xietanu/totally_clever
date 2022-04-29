"""Tests for the Die component class"""
from dataclasses import dataclass
import enum
import random
import arcade

import colours
from components import clickable, coords
import game
import scenes
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


class Die(clickable.Clickable):
    """Class for die component"""

    def __init__(
        self,
        center: coords.Coords,
        colour: tuple[int, int, int] = colours.Category.SKY.value,
        **sprite_kwargs
    ):

        self.sprite = arcade.Sprite(
            filename=sprites.filepaths.DiceSpriteList.DIE.value,
            image_width=64,
            image_height=64,
            center_x=center.x_coord,
            center_y=center.y_coord,
            **sprite_kwargs
        )

        self.selected_sprite = arcade.Sprite(
            filename=sprites.filepaths.DiceSpriteList.HIGHLIGHT.value,
            center_x=self.sprite.center_x,
            center_y=self.sprite.center_y,
        )
        self.selected_sprite.visible = False

        game.TotallyClever().add_sprites_to_layer(
            [self.sprite, self.selected_sprite], scenes.MainGameLayers.DICE
        )

        self.colour = colour
        self.sprite.color = colour
        self.side = 1
        self.timer = 0

        self.mode = DieModes.ROLLING

        self.sprite.textures = arcade.load_spritesheet(
            "images/dice_sprite_sheet.png",
            sprite_width=64,
            sprite_height=64,
            columns=6,
            count=6,
        )
        self.texture = self.sprite.textures[self.side - 1]

    def update_animation(self, delta_time: float = 1 / 60):
        """Updates the dice's visuals while rolling"""
        if self.mode == DieModes.ROLLING:
            self.timer += delta_time
            if self.timer > 0.15:
                self.timer = 0
                new_side = random.randrange(5)
                if new_side >= self.side:
                    new_side += 1
                self._set_side(new_side)

    def on_mouse_press(self) -> bool:
        """Defines behaviour when clicked on"""
        if self.mode in [DieModes.BASE]:
            self.mode = DieModes.SELECTED
            self.selected_sprite.visible = True
            return True
        if self.mode == DieModes.SELECTED:
            self.reset_selection()
        return False

    def reset_selection(self):
        """Reset whether the die is selected"""
        self.mode = DieModes.BASE
        self.selected_sprite.visible = False

    def roll(self) -> None:
        """
        Randomise the side of the die
        """
        self._set_side(random.randrange(6) + 1)
        self.mode = DieModes.BASE

    def start_rolling(self) -> None:
        """
        Start the rolling animation.
        """
        self.mode = DieModes.ROLLING

    def _set_side(self, value: int) -> None:
        """
        Set the side of the die to the specified value

        Args:
            value (int): value on the die
        """

        self.side = value
        self.sprite.texture = self.sprite.textures[self.side - 1]
