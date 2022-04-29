"""Contains enums for standard sprites used in the game"""

from enum import Enum


class ZoneSprite(Enum):
    """Provides filepaths to standard score category sprites"""

    SHORT = "images/short_area.png"

class DiceSpriteList(Enum):
    """Filepaths for dice related sprites"""
    DIE = "images/dice_sprite_sheet.png"
    HIGHLIGHT = "images/dice_highlight.png"