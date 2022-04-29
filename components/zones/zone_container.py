"""ZoneContainer class"""
from components.zones import at_least, in_order_sum

from components import coords, boxes

import sprites
import colours


class ZoneContainer:
    """Class that contains and creates the score zones used in the game."""

    def __init__(self, origin: coords.Coords) -> None:
        self.origin = origin
        self.at_least = self._create_at_least_zone()
        self.greater_than_last_zone = self._create_greater_than_last_zone()
        self.multiplier_zone = self._create_mutliplier_zone()

    def __iter__(self):
        return iter([self.at_least, self.greater_than_last_zone])

    def _create_at_least_zone(self) -> at_least.AtLeastZone:
        """
        Creates the 'At least X' score zone

        Returns:
            AtLeastZone: Created zone
        """
        new_at_least = at_least.AtLeastZone(
            filename=sprites.filepaths.ZoneSprite.SHORT.value,
            colour=colours.Category.SUNGLOW.value,
            origin=self.origin,
        )

        new_at_least.add_decorative_sprite(
            "images/arrow_icon.png", coords.Coords(30, 50), apply_color=True
        )

        for x_offset, min_value in enumerate(list(range(1, 6)) + list(range(1, 7))):
            new_at_least.add_box(
                offset=coords.Coords(70 + 40 * x_offset, 50),
                min_value=min_value,
            )

        return new_at_least

    def _create_greater_than_last_zone(self) -> in_order_sum.InOrderSumZone:
        """
        Creates the 'Greater than last' score zone

        Returns:
            InOrderSumZone: Created zone
        """
        greater_than_last_zone = in_order_sum.InOrderSumZone(
            filename=sprites.filepaths.ZoneSprite.SHORT.value,
            colour=colours.Category.SKY.value,
            origin=self.origin + coords.Coords(0, 300),
        )

        greater_than_last_zone.add_decorative_sprite(
            "images/arrow_icon.png", coords.Coords(30, 50), apply_color=True
        )

        for x_offset in range(11):
            greater_than_last_zone.add_box(
                boxes.GreaterThanPrereqBox,
                coords.Coords(70 + 40 * x_offset, 50),
            )

        return greater_than_last_zone

    def _create_mutliplier_zone(self):
        multiplier_zone = in_order_sum.InOrderSumZone(
            filename=sprites.filepaths.ZoneSprite.SHORT.value,
            colour=colours.Category.ALABASTER.value,
            origin=self.origin + coords.Coords(0, 150),
        )

        multiplier_zone.add_decorative_sprite(
            "images/arrow_icon.png", coords.Coords(30, 50), apply_color=True
        )

        for x_offset, multiplier in enumerate([1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 3]):
            multiplier_zone.add_box(
                boxes.MultiplierBox,
                offset=coords.Coords(70 + 40 * x_offset, 50),
                multiplier=multiplier,
            )

        return multiplier_zone
