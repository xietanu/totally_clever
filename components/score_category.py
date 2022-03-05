"""Score cateogry class"""
from enum import Enum

from arcade import SpriteList, get_sprites_at_point
from abstracts.coords import Coords

from abstracts.multi_sprite import MultiSprite
from components.markable_box import MarkableBox


class ScoreModes(Enum):
    """Provides the score mode for the different categories"""

    SUM = 1
    COUNT = 2
    MATCHED = 3


class MarkPrereqMode(Enum):
    """Provides the mode to determine how boxes become available"""

    PREVIOUS = 1
    NONE = 0


class ScoreCategory(MultiSprite):
    """A general class for the scoring categories for specific colours to build on top of"""

    def __init__(
        self,
        filename: str,
        origin: Coords,
        score_mode: Enum = ScoreModes.SUM,
        mark_prereq_mode: Enum = MarkPrereqMode.NONE,
        **MultiSpriteArgs
    ):
        super().__init__(filename=filename, **MultiSpriteArgs)
        self.origin = origin
        self.center_x = origin.x_coord + int(self.texture.size[0] / 2)
        self.center_y = origin.y_coord + int(self.texture.size[1] / 2)

        self.boxes = SpriteList(use_spatial_hash=True)

        self.score_mode = score_mode
        self.score_trackers = None
        if score_mode.value in [ScoreModes.MATCHED.value, ScoreModes.COUNT.value]:
            self.score_trackers = SpriteList(use_spatial_hash=True)

        self.mark_prereq_mode = mark_prereq_mode

    def add_box(
        self,
        offset:Coords,
        text: str = "",
    ):
        """Add a new box to the score category, with x and y set relative to the box"""
        prereq = None
        if (
            self.mark_prereq_mode.value == MarkPrereqMode.PREVIOUS.value
            and len(self.boxes) > 0
        ):
            prereq = self.boxes[-1]

        box = MarkableBox(
            self,
            center=self.origin + offset,
            text=text,
            prereq=prereq,
        )
        if (
            self.mark_prereq_mode.value == MarkPrereqMode.NONE.value
            or len(self.boxes) == 0
        ):
            box.markable = True

        self.boxes.append(box)
        self.sub_sprites.append(box)

    def on_mouse_press(self, pointer: Coords):
        """Manages click on the score_category"""
        boxes = get_sprites_at_point((pointer.x_coord, pointer.y_coord), self.boxes)

        if len(boxes) > 0:
            boxes[0].mark_box()

    def update_markables(self):
        """Update the markable status for all boxes"""
        for box in self.boxes:
            box.update_markable()
