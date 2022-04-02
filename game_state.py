"""GameState enum"""
import enum


class State(enum.Enum):
    """Enumerated game state"""

    ROLLING = enum.auto()
    SELECTING_DIE = enum.auto()
