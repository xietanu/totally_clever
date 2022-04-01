"""Score category class"""
from arcade import Sprite
from arcade.sprite_list.sprite_list import SpriteList
from arcade.sprite_list.spatial_hash import get_sprites_at_point
from abstracts.coords import Coords

from abstracts.multi_sprite import MultiSprite
from components.markable_box import MarkableBox


class ScoreCategory(MultiSprite):
    """A general class for the scoring categories for specific colours to build on top of"""

    def __init__(
        self,
        filename: str,
        colour: tuple[int, int, int],
        origin: Coords,
        **MultiSpriteArgs
    ):
        super().__init__(filename=filename, **MultiSpriteArgs)
        self.origin = origin
        self.center_x = origin.x_coord + int(self.texture.size[0] / 2)
        self.center_y = origin.y_coord + int(self.texture.size[1] / 2)

        self.boxes = SpriteList(use_spatial_hash=True)

        self.color = colour

        self.score_trackers = None

    def add_box(
        self,
        offset: Coords,
        label: str = "",
    ) -> MarkableBox:
        """Add a new box to the score category, with x and y set relative to the box"""
        box = MarkableBox(self, center=self.origin + offset, text=label)

        if len(self.boxes) == 0:
            box.markable = True

        self.boxes.append(box)
        self.sub_sprites.append(box)

        return box

    def add_decorative_sprite(
        self, filename, offset: Coords, *, apply_color: bool = False
    ):
        """Add a decorative sprite to the ScoreCategory."""
        position = self.origin + offset

        new_sprite = Sprite(
            filename, center_x=position.x_coord, center_y=position.y_coord
        )

        if apply_color:
            new_sprite.color = self.color

        self.sub_sprites.append(new_sprite)

    def on_mouse_press(self, pointer: Coords):
        """Manages click on the score_category"""
        boxes = get_sprites_at_point((pointer.x_coord, pointer.y_coord), self.boxes)

        if len(boxes) > 0 and isinstance(boxes[0], MarkableBox):
            boxes[0].mark_box()

    def update_markables(self) -> None:
        """Update the markable status for all boxes"""
        for box in self.boxes:
            if isinstance(box, MarkableBox):
                box.update_markable()

    def get_score(self) -> int:
        """
        Calculates and returns the score for this category.
        Not implemented for parent class.

        Returns:
            int: The calculated score.
        """
        raise NotImplementedError(
            "Score category subclass should provide own get_score method"
        )
