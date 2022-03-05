"""Score cateogry class"""
from enum import Enum

from arcade import SpriteList

from abstracts.multi_sprite import MultiSprite
from components.markable_box import MarkableBox


class ScoreModes(Enum):
    """Provides the score mode for the different categories"""

    SUM = 1
    COUNT = 2
    MATCHED = 3


class ScoreCategory(MultiSprite):
    """A general class for the scoring categories for specific colours to build on top of"""

    def __init__(
        self,
        filename: str,
        start_x: int,
        start_y: int,
        score_mode: Enum = ScoreModes.SUM,
        **MultiSpriteArgs
    ):
        super().__init__(filename=filename, **MultiSpriteArgs)
        self.start_x = start_x
        self.start_y = start_y
        self.center_x = start_x + int(self.texture.size[0] / 2)
        self.center_y = start_y + int(self.texture.size[1] / 2)

        self.boxes = SpriteList(use_spatial_hash=True)

        self.score_mode = score_mode
        self.score_trackers = None
        if score_mode.value in [ScoreModes.MATCHED.value, ScoreModes.COUNT.value]:
            self.score_trackers = SpriteList(use_spatial_hash=True)

    def add_box(self, offset_x: int, offset_y: int, text: str = ""):
        """Add a new box to the score category, with x and y set relative to the box"""
        box = MarkableBox(self, self.start_x + offset_x, self.start_y + offset_y, text)
        self.boxes.append(box)
        self.sub_sprites.append(box)
