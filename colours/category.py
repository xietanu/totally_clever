"""Colour and Colours"""
from enum import Enum

from colours import convert


class Category(Enum):
    """Holds the colours used for the main categories in the game"""

    SKY = convert.hex_colour_to_rgb_tuple("75CDD8")
    ALABASTER = convert.hex_colour_to_rgb_tuple("F0F2E7")
    SALMON = convert.hex_colour_to_rgb_tuple("FF8296")
    SUNGLOW = convert.hex_colour_to_rgb_tuple("FFCA27")
    LIBERTY = convert.hex_colour_to_rgb_tuple("6257B2")
