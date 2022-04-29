"""MultiplierBox class"""
from typing import Optional

from components import coords, die

from components.boxes import create_text_mark_sprite, markable_box
from components.zones import zone


class MultiplierBox(markable_box.MarkableBox):
    """Box class scored based the value assigned to it. Can apply a multiplier"""

    def __init__(
        self,
        parent_zone: "zone.Zone",
        center: coords.Coords,
        prereq_box: Optional[markable_box.MarkableBox] = None,
        multiplier: int = 1,
        text: str = "",
    ):
        super().__init__(parent_zone, center, prereq_box, f"x{multiplier}" if multiplier > 1 else "")
        self.marked_value = 0
        self.multiplier = multiplier

    def try_mark(self, selected_die: die.Die) -> bool:
        """
        Try marking the box, returns whether successful

        Args:
            value (int): value of the die to mark the box

        Returns:
            bool: Whether box has been marked
        """
        if self.prereq_box and not self.prereq_box.marked and not super().try_mark(selected_die):
            return False
        
        value = selected_die.side

        self.set_text("")

        self.marked_value = value * self.multiplier

        self.mark_sprite = create_text_mark_sprite.create_text_mark_sprite(
            self.marked_value, coords.Coords(self.center_x, self.center_y)
        )
        return True

    def get_score(self) -> int:
        """
        Get the score associated with this box.

        Returns:
            int: score from box. 0 if not marked.
        """
        return self.marked_value
