"""Markable box class"""
from typing import Optional
import arcade
from components import coords
import sprites


class MarkableBox(sprites.MultiSprite):
    """Class for boxes that can be marked"""

    def __init__(self, prereq_box: Optional["MarkableBox"] = None):
        super().__init__(filename="images/mark_box.png", center_x=0, center_y=0)
        self.marked = False

        self.mark_sprite = arcade.Sprite(
            filename="images/mark_box_mark.png",
            hit_box_algorithm="None",
        )

        self._text = ""
        self._text_sprite = None

        self.prereq_box = prereq_box

    def set_pos(self, position: coords.Coords) -> None:
        """
        Set the position of the markable box

        Args:
            position (coords.Coords): New coordinates of the box
        """
        self.center_x = position.x_coord
        self.center_y = position.y_coord
        if self.mark_sprite:
            self.mark_sprite.center_x = position.x_coord
            self.mark_sprite.center_y = position.y_coord
        if self._text_sprite:
            self._text_sprite.center_x = position.x_coord
            self._text_sprite.center_y = position.y_coord

    def try_mark(self, value: int) -> bool:  ## pylint: disable=unused-argument
        """
        Try marking the box, returns whether successful

        Returns:
            bool: Whether box has been marked
        """
        if self.marked:
            return False

        self.marked = True
        self.sub_sprites.append(self.mark_sprite)
        return True

    @property
    def label(self) -> str:
        """
        Get the text label on the box

        Returns:
            str: label
        """
        return self._text

    @label.setter
    def label(self, new_label: str) -> None:
        """
        Set the text label for the box

        Args:
            new_label (str): new label
        """
        self._text = new_label

        if self._text_sprite:
            self._text_sprite.remove_from_sprite_lists()

        self._text_sprite = arcade.create_text_sprite(
            text=new_label,
            start_x=self.center_x,
            start_y=self.center_y,
            bold=True,
            color=(0, 0, 0),
            anchor_x="center",
            anchor_y="center",
        )
        self.sub_sprites.append(self._text_sprite)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return 1 if self.marked else 0
