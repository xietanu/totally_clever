"""Class for the score zone where dice need to increase."""
from components.zones import zone
from components import coords
from components.boxes import markable_box


class InOrderSumZone(zone.Zone):
    """Zone where the boxes are filled in in order and the score is equal to their sum"""

    def add_box(self, box: markable_box.MarkableBox, offset: coords.Coords) -> None:
        """
        Add a markable box to this zone.

        Args:
            offset (Coords): Offset from the bottom left corner of the zone.
            label (str, optional): Text label to draw on the markable box. Defaults to "".
        """
        if self.boxes:
            last_box = self.boxes[-1]
            if isinstance(last_box, markable_box.MarkableBox):
                box.prereq_box = last_box

        super().add_box(box, offset)

    def get_score(self) -> int:
        """
        Calculates and returns the score for this category.

        Returns:
            int: The calculated score.
        """
        return sum(
            [
                box.get_score()
                for box in self.boxes
                if isinstance(box, markable_box.MarkableBox)
            ]
        )
