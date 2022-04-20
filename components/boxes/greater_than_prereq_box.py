"""GreaterThanPrereqBox class"""
from typing import Optional

from components import coords

from components.boxes import create_text_mark_sprite, markable_box


class GreaterThanPrereqBox(markable_box.MarkableBox):
    """Markable box where the value must be greater than the previous box"""

    def __init__(
        self,
        prereq_box: Optional["GreaterThanPrereqBox"] = None,
    ):
        super().__init__(prereq_box)
        self.marked_value = 0
        self.mark_sprite = None

    def try_mark(self, value: int) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        if isinstance(self.prereq_box, GreaterThanPrereqBox) and (
            not self.prereq_box.marked
            or (
                self.prereq_box.marked_value >= value
                and self.prereq_box.marked_value < 6
            )
        ):
            return False

        self.mark_sprite = create_text_mark_sprite.create_text_mark_sprite(
            value, coords.Coords(self.center_x, self.center_y)
        )

        self.marked_value = value

        return super().try_mark(value)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return self.marked_value
