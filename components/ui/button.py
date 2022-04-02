"""Button class"""
import arcade
import sprites
from components import coords
from components.ui import button_ids


class Button(sprites.MultiSprite):
    """Class for clickable button to trigger behaviour"""

    def __init__(
        self,
        button_id: int,
        center: coords.Coords,
        text: str,
        colour: tuple[int, int, int],
    ):
        super().__init__(
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
            color=(255, 255, 255),
            anchor_x="center",
            anchor_y="center",
        )

        self.sub_sprites.append(self._text_sprite)

    def matches(self, id_to_check: button_ids.ButtonID) -> bool:
        """
        Check if the id of this button matches the provided id.

        Args:
            id_to_check (ButtonID): ButtonID enum to check

        Returns:
            bool: Whether it is a match
        """
        return self.identifier == id_to_check.value

    @property
    def label(self) -> str:
        """
        Get the text written on the button

        Returns:
            str: Button's text
        """
        return self._text

    @label.setter
    def set_label(self, text: str):
        """
        Sets the text written on the button.

        Args:
            text (str): Nex text for the button
        """
        self._text = text

        self._text_sprite.remove_from_sprite_lists()

        self._text_sprite = arcade.create_text_sprite(
            text,
            start_x=self.center_x,
            start_y=self.center_y,
            font_size=32,
            bold=True,
            color=(255, 255, 255),
            anchor_x="center",
            anchor_y="center",
        )

        self.sub_sprites.append(self._text_sprite)
