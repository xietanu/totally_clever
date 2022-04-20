"""MinValueBox class"""
from typing import Optional

from components.boxes import markable_box


class MinValueBox(markable_box.MarkableBox):
    """Markable box where a minimum value must be met"""

    def __init__(
        self,
        min_value: int = 0,
        prereq_box: Optional[markable_box.MarkableBox] = None,
    ):
        super().__init__(prereq_box)
        self.min_value = min_value
        self.label = f"\u2265{min_value}"

    def try_mark(self, value: int) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        if value < self.min_value or (self.prereq_box and not self.prereq_box.marked):
            return False

        return super().try_mark(value)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        # TODO: Implement this
        return 1 if self.marked else 0
