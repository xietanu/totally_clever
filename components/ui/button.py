"""Button class"""
import arcade
import colours
from components import clickable, coords
from components.ui import button_ids
import scenes
import game

class Button(clickable.Clickable):
    """Class for clickable button to trigger behaviour"""

    def __init__(
        self,
        button_id: int,
        center: coords.Coords,
        text: str,
        colour: tuple[int, int, int],
    ):
        self.sprite = arcade.Sprite(
            filename="images/basic_button.png",
            center_x=center.x_coord,
            center_y=center.y_coord,
        )
        self.identifier = button_id
        self.color = colour

        self._text = text

        self._text_sprite = arcade.create_text_sprite(
            text,
            start_x=center.x_coord,
            start_y=center.y_coord,
            font_size=32,
            bold=True,
            color=colours.Contrast.WHITE.value,
            anchor_x="center",
            anchor_y="center",
        )

        game.TotallyClever().add_sprites_to_layer(
            [self.sprite, self._text_sprite], scenes.MainGameLayers.UI
        )

    def matches(self, id_to_check: button_ids.ButtonID) -> bool:
        """
        Check if the id of this button matches the provided id.

        Args:
            id_to_check (ButtonID): ButtonID enum to check

        Returns:
            bool: Whether it is a match
        """
        return self.identifier == id_to_check.value
