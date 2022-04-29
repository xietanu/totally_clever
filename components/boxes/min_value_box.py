"""MinValueBox class"""
from typing import Optional
from components import coords, die

from components.boxes import markable_box
from components.zones import zone

class MinValueBox(markable_box.MarkableBox):
    """Markable box where a minimum value must be met"""

    def __init__(
        self,
        parent_zone: "zone.Zone",
        center: coords.Coords,
        prereq_box: Optional[markable_box.MarkableBox] = None,
        min_value: int = 0,
        text: str = "",
    ):
        super().__init__(parent_zone, center, prereq_box, f"\u2265{min_value}")
        self.min_value = min_value

    def try_mark(self, selected_die: die.Die) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        value = selected_die.side
        
        if value < self.min_value or (self.prereq_box and not self.prereq_box.marked):
            return False

        return super().try_mark(selected_die)

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        # TODO: Implement this
        return 1 if self.marked else 0
