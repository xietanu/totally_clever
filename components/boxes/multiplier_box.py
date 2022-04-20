"""MultiplierBox class"""
from typing import Optional

import arcade

from components.boxes import markable_box
import colours


class MultiplierBox(markable_box.MarkableBox):
    """Box class scored based the value assigned to it. Can apply a multiplier"""

    def __init__(
        self,
        multiplier: int = 1,
        prereq_box: Optional[markable_box.MarkableBox] = None,
    ):
        super().__init__()
        self.prereq_box = prereq_box
        self.marked_value = 0
        self.mark_sprite = None
        self.multiplier = multiplier
        if multiplier > 1:
            self.label = f"x{multiplier}"

    def try_mark(self, value: int) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        if self.prereq_box and not self.prereq_box.marked:
            return False

        self.label = ""

        self.marked_value = value * self.multiplier

        self.mark_sprite = arcade.create_text_sprite(
            text=str(self.marked_value),
            start_x=self.center_x,
            start_y=self.center_y,
            bold=True,
            color=colours.Contrast.RUBY.value,
            anchor_x="center",
            anchor_y="center",
            font_size=18,
        )

        return super().try_mark(value)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return self.marked_value
