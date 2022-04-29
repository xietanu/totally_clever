"""Class for the score zone with minimum requirements"""
from components.zones import zone
from components import coords, boxes


class AtLeastZone(zone.Zone):
    """Score zone with minimum requirements"""

    def add_box(self, offset: coords.Coords, min_value: int) -> boxes.MarkableBox:
        """
        Add a markable box to this zone.

        Args:
            offset (Coords): Offset from the bottom left corner of the zone.
            label (str, optional): Text label to draw on the markable box. Defaults to "".
        """
        return super().add_box(
            boxes.MinValueBox,
            offset=offset,
            prereq_box=self.boxes[-1] if self.boxes else None,
            min_value=min_value
        )

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
                if isinstance(box, boxes.MarkableBox)
            ]
        )
