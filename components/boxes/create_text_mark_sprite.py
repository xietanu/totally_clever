"""create_text_mark_sprite function"""
from typing import Union
import arcade
import colours

from components import coords


def create_text_mark_sprite(
    text: Union[str, int], center: coords.Coords
) -> arcade.Sprite:
    """
    Create a standard sprite for marking a box with text.

    Args:
        text (Union[str, int]): The text to use as the mark
        center (coords.Coords): The center coordinates of the mark.

    Returns:
        arcade.Sprite: _description_
    """
    return arcade.create_text_sprite(
        text=str(text),
        start_x=center.x_coord,
        start_y=center.y_coord,
        bold=True,
        color=colours.Contrast.RUBY.value,
        anchor_x="center",
        anchor_y="center",
        font_size=18,
    )
