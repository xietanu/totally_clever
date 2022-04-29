"""GreaterThanPrereqBox class"""
from typing import Optional

from components import coords, die

from components.boxes import create_text_mark_sprite, markable_box
from components.zones import zone


class GreaterThanPrereqBox(markable_box.MarkableBox):
    """Markable box where the value must be greater than the previous box"""

    def __init__(
        self,
        parent_zone: "zone.Zone",
        center: coords.Coords,
        prereq_box: Optional["GreaterThanPrereqBox"] = None,
        text: str = "",
    ):
        super().__init__(parent_zone, center, prereq_box, text)
        self.marked_value = 0
        self.mark_sprite = None

    def try_mark(self, selected_die: die.Die) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        value = selected_die.side

        if isinstance(self.prereq_box, GreaterThanPrereqBox) and (
            not self.prereq_box.marked
            or (
                self.prereq_box.marked_value >= value
                and self.prereq_box.marked_value < 6
            )
            and not super().try_mark(selected_die)
        ):
            return False

        self.mark_sprite = create_text_mark_sprite.create_text_mark_sprite(
            value, coords.Coords(self.center_x, self.center_y)
        )

        self.marked_value = value

        return True

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return self.marked_value
