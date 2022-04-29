"""MainGameLayers class"""
from enum import Enum

class MainGameLayers(str, Enum):
    """List of layers in the main game scene"""

    PAPER_BASE = "paper_base"
    PAPER_INTERACTIVE = "paper_interactive"
    DICE = "dice"
    UI = "ui"
