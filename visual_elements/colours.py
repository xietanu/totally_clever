"""Colour and Colours"""
from dataclasses import dataclass
from enum import Enum

from visual_elements.hex_color_to_rgb_tuple import hex_colour_to_rgb_tuple


@dataclass
class Colour:
    """Holds colours and their tones"""

    base: tuple[int, int, int]
    light: tuple[int, int, int]
    dark: tuple[int, int, int]


class Colours(Enum):
    """Holds the colours used in the game"""

    SKY = hex_colour_to_rgb_tuple("75CDD8")
    ALABASTER = hex_colour_to_rgb_tuple("F0F2E7")
    SALMON = hex_colour_to_rgb_tuple("FF8296")
    SUNGLOW = hex_colour_to_rgb_tuple("FFCA27")
    LIBERTY = hex_colour_to_rgb_tuple("6257B2")
