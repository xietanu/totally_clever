"""Score zone classes for each category"""
import arcade
from components import coords, markable_box
import sprites


class Zone(sprites.MultiSprite):
    """A general class for the scoring categories for specific colours to build on top of"""

    def __init__(
        self,
        filename: str,
        colour: tuple[int, int, int],
        origin: coords.Coords,
        **MultiSpriteArgs
    ):
        super().__init__(filename=filename, **MultiSpriteArgs)
        self.origin = origin
        self.center_x = origin.x_coord + int(self.texture.size[0] / 2)
        self.center_y = origin.y_coord + int(self.texture.size[1] / 2)

        self.boxes = arcade.SpriteList(use_spatial_hash=True)

        self.color = colour

        self.score_trackers = None

    def add_box(
        self,
        offset: coords.Coords,
        label: str = "",
    ) -> markable_box.MarkableBox:
        """Add a new box to the score category, with x and y set relative to the box"""
        box = markable_box.MarkableBox(self, center=self.origin + offset, text=label)

        if len(self.boxes) == 0:
            box.markable = True

        self.boxes.append(box)
        self.sub_sprites.append(box)

        return box

    def add_decorative_sprite(
        self, filename, offset: coords.Coords, *, apply_color: bool = False
    ):
        """Add a decorative sprite to the ScoreCategory."""
        position = self.origin + offset

        new_sprite = arcade.Sprite(
            filename, center_x=position.x_coord, center_y=position.y_coord
        )

        if apply_color:
            new_sprite.color = self.color

        self.sub_sprites.append(new_sprite)

    def on_mouse_press(self, pointer: coords.Coords):
        """Manages click on the score_category"""
        boxes = arcade.get_sprites_at_point(
            (pointer.x_coord, pointer.y_coord), self.boxes
        )

        if len(boxes) > 0 and isinstance(boxes[0], markable_box.MarkableBox):
            boxes[0].mark_box()

    def update_markables(self) -> None:
        """Update the markable status for all boxes"""
        for markable in self.boxes:
            if isinstance(markable, markable_box.MarkableBox):
                markable.update_markable()

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
