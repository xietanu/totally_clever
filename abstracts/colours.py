"""Colour and Colours"""
from dataclasses import dataclass
from enum import Enum

from abstracts.hex_color_to_rgb_tuple import hex_colour_to_rgb_tuple


@dataclass
class Colour:
    """Holds colours and their tones"""

    base: tuple[int, int, int]
    light: tuple[int, int, int]
    dark: tuple[int, int, int]


class Colours(Enum):
    """Holds the colours used in the game"""

    SAPPHIRE = Colour(
        base=hex_colour_to_rgb_tuple("086788"),
        light=hex_colour_to_rgb_tuple("18BBF2"),
        dark=hex_colour_to_rgb_tuple("043B4D"),
    )
    FLAME = Colour(
        base=hex_colour_to_rgb_tuple("E4572E"),
        light=hex_colour_to_rgb_tuple("EC8C6F"),
        dark=hex_colour_to_rgb_tuple("5A1E0C"),
    )
    TIFFANY = Colour(
        base=hex_colour_to_rgb_tuple("17C3B2"),
        light=hex_colour_to_rgb_tuple("5BECDD"),
        dark=hex_colour_to_rgb_tuple("0B5B63"),
    )
    SAND = Colour(
        base=hex_colour_to_rgb_tuple("F4D06F"),
        light=hex_colour_to_rgb_tuple("FAE7B3"),
        dark=hex_colour_to_rgb_tuple("BE8F0E"),
    )
    BONE = Colour(
        base=hex_colour_to_rgb_tuple("FFF8F0"),
        light=hex_colour_to_rgb_tuple("FFFFFF"),
        dark=hex_colour_to_rgb_tuple("FFD9AD"),
    )
