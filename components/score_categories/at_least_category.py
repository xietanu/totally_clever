"""Class for score category of ascending requirements"""

from abstracts.coords import Coords
from components.markable_box import MarkableBox
from components.score_categories.score_category import ScoreCategory


class AtLeastCategory(ScoreCategory):
    """Score category of ascending requirements"""

    def add_box(self, offset: Coords, label: str = "") -> MarkableBox:
        """
        Add a markable box to this score category.

        Args:
            offset (Coords): Offset from the bottom left corner of the score score category.
            label (str, optional): Text label to draw on the markable box. Defaults to "".

        Returns:
            MarkableBox: The box that has been added to the score category.
        """
        box = super().add_box(offset, label)

        if len(self.boxes) > 1:
            box.set_prereq(self.boxes[-2])

    def get_score(self) -> int:
        """
        Calculates and returns the score for this category.

        Returns:
            int: The calculated score.
        """
        return sum([1 if box.marked else 0 for box in self.boxes])  # To implement
