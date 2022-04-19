"""Contrasting colours"""
from enum import Enum

from colours import convert


class Contrast(Enum):
    """Contrasting colours to category colours."""

    RUBY = convert.hex_colour_to_rgb_tuple("#A4031F")
