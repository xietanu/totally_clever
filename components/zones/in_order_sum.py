"""Class for the score zone where dice need to increase."""
from components.zones import zone
from components import coords
from components.boxes import markable_box


class InOrderSumZone(zone.Zone):
    """Zone where the boxes are filled in in order and the score is equal to their sum"""

    def add_box(
        self, box_type: type, offset: coords.Coords, **box_type_kwargs
    ) -> markable_box.MarkableBox:
        """
        Add a markable box to this zone.

        Args:
            offset (Coords): Offset from the bottom left corner of the zone.
            label (str, optional): Text label to draw on the markable box. Defaults to "".
        """
        return super().add_box(
            box_type,
            offset=offset,
            prereq_box=self.boxes[-1] if self.boxes else None,
            **box_type_kwargs
        )

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
