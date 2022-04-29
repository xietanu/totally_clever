"""Score zone classes for each category"""
from typing import Optional
import arcade
from components import coords, boxes
import scenes
import game

class Zone():
    """A general class for the scoring categories for specific colours to build on top of"""

    def __init__(
        self,
        filename: str,
        colour: tuple[int, int, int],
        origin: coords.Coords,
    ):
        self.sprite = arcade.Sprite(filename=filename)
        if isinstance(self.sprite.texture, arcade.Texture):
            self.sprite.center_x = origin.x_coord + int(self.sprite.texture.size[0] / 2)
            self.sprite.center_y = origin.y_coord + int(self.sprite.texture.size[1] / 2)

        self.origin = origin

        self.boxes = []

        self.color = colour

    def add_box(
        self,
        box_class: type,
        offset: coords.Coords,
        prereq_box: Optional[boxes.MarkableBox] = None,
        text: str = "",
        **subclass_kwargs,
    ) -> boxes.MarkableBox:
        """
        Add a new markable box to this zone.

        Args:
            box_class (type): Subclass of MarkableBox to use to create the box.
            offset (coords.Coords): Offset of the center of the box from
                the bottom left of the zone.
            prereq_box (Optional[boxes.MarkableBox], optional): Pre-requisite box to be marked
                before this one can be marked. Defaults to None.
            text (str, optional): Text to put in the box. Defaults to "".
            **subclass_kwargs: Any additional keyword arguments for the box subclass.

        Raises:
            ValueError: Raised if the box_class is not a subclass of MarkableBox.

        Returns:
            boxes.MarkableBox: The newly created box instance.
        """
        if not issubclass(box_class, boxes.MarkableBox):
            raise ValueError(
                f"Received class {boxes.MarkableBox} to add a box, should be a MarkableBox."
            )

        new_box = box_class(
            self,
            center=self.origin + offset,
            prereq_box=prereq_box,
            text=text,
            **subclass_kwargs,
        )

        self.boxes.append(new_box)

        return new_box

    def add_decorative_sprite(
        self, filename:str, offset: coords.Coords, *, apply_color: bool = False
    ) -> None:
        """
        Add a decorative sprite to the zone.

        Args:
            filename (str): The filename and path for the image for the sprite.
            offset (coords.Coords): Center of the sprite, measured from the
                bottom left of the zone.
            apply_color (bool, optional): Whether to colourize the sprite in line with the zone.
                Defaults to False.
        """
        position = self.origin + offset

        new_sprite = arcade.Sprite(
            filename, center_x=position.x_coord, center_y=position.y_coord
        )

        if apply_color:
            new_sprite.color = self.color

        game.TotallyClever().add_sprites_to_layer(new_sprite, scenes.MainGameLayers.PAPER_BASE)

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
