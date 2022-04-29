"""Markable box class"""
from typing import Optional
import arcade
from components import coords, die, clickable
import game
import scenes

class MarkableBox(clickable.Clickable):
    """Class for boxes that can be marked"""

    def __init__(
        self,
        parent_zone,
        center: coords.Coords,
        prereq_box: Optional["MarkableBox"] = None,
        text: str = "",
    ):
        self.sprite = arcade.Sprite(
            filename="images/mark_box.png",
            center_x=center.x_coord,
            center_y=center.y_coord,
        )
        self.marked = False
        self.zone = parent_zone

        self.mark_sprite = arcade.Sprite(
            filename="images/mark_box_mark.png",
            hit_box_algorithm="None",
        )
        self.mark_sprite.visible = False

        game.TotallyClever().add_sprites_to_layer(self.sprite, scenes.MainGameLayers.PAPER_BASE)
        game.TotallyClever().add_sprites_to_layer(
            self.mark_sprite, scenes.MainGameLayers.PAPER_INTERACTIVE
        )

        self.prereq_box = prereq_box

        self._text = ""
        self._text_sprite = None
        if text:
            self.set_text(text)

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

    def try_mark(self, selected_die: die.Die) -> bool:
        """
        Try marking the box, returns whether successful

        Returns:
            bool: Whether box has been marked
        """
        if self.marked or self.zone.color != selected_die.color:
            return False

        self.marked = True
        self.mark_sprite.visible = True
        return True

    def set_text(self, text: str) -> None:
        """
        Set the text label for the box

        Args:
            text (str): new label
        """
        self._text = text

        if self._text_sprite:
            self._text_sprite.remove_from_sprite_lists()

        self._text_sprite = arcade.create_text_sprite(
            text=text,
            start_x=self.sprite.center_x,
            start_y=self.sprite.center_y,
            bold=True,
            color=(0, 0, 0),
            anchor_x="center",
            anchor_y="center",
        )
        game.TotallyClever().add_sprites_to_layer(self._text_sprite, scenes.MainGameLayers.PAPER_BASE)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return 1 if self.marked else 0
