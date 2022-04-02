"""Class for the score zone with minimum requirements"""
from components.zones import zone
from components import coords
from components.boxes import markable_box, min_value_box


class AtLeast(zone.Zone):
    """Score zone with minimum requirements"""

    def add_box(self, box: min_value_box.MinValueBox, offset: coords.Coords) -> None:
        """
        Add a markable box to this zone.

        Args:
            offset (Coords): Offset from the bottom left corner of the zone.
            label (str, optional): Text label to draw on the markable box. Defaults to "".

        Returns:
            MarkableBox: The box that has been added to the score category.
        """
        if self.boxes:
            last_box = self.boxes[-1]
            if isinstance(last_box, min_value_box.MinValueBox):
                box.prereq_box = last_box

        super().add_box(box, offset)

    def get_score(self) -> int:
        """
        Calculates and returns the score for this category.

        Returns:
            int: The calculated score.
        """
        # TODO: Implement
        return sum(
            [
                1 if box.marked else 0
                for box in self.boxes
                if isinstance(box, markable_box.MarkableBox)
            ]
        )
