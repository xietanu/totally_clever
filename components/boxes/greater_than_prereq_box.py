"""MinValueBox class"""
from typing import Optional

import arcade

from components.boxes import markable_box
import colours


class GreaterThanPrereqBox(markable_box.MarkableBox):
    """Markable box where a minimum value must be met"""

    def __init__(
        self,
        prereq_box: Optional["GreaterThanPrereqBox"] = None,
    ):
        super().__init__()
        self.prereq_box = prereq_box
        self.marked_value = 0
        self._text_sprite = None

    def try_mark(self, value: int) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        if self.prereq_box and (
            not self.prereq_box.marked or self.prereq_box.marked_value >= value
        ):
            return False

        self._text_sprite = arcade.create_text_sprite(
            text=str(value),
            start_x=self.center_x,
            start_y=self.center_y,
            bold=True,
            color=colours.Contrast.RUBY.value,
            anchor_x="center",
            anchor_y="center",
        )

        return super().try_mark(value)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return self.marked_value
