"""Colour and Colours"""
from enum import Enum

import arcade


class Category(Enum):
    """Holds the colours used for the main categories in the game"""

    SKY = arcade.color_from_hex_string("75CDD8")
    ALABASTER = arcade.color_from_hex_string("F0F2E7")
    SALMON = arcade.color_from_hex_string("FF8296")
    SUNGLOW = arcade.color_from_hex_string("FFCA27")
    LIBERTY = arcade.color_from_hex_string("6257B2")
