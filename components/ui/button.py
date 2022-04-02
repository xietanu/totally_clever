"""Button class"""
import arcade
from components import coords
import game_state
import sprites


class Button(sprites.MultiSprite):
    """Class for clickable button to trigger behaviour"""

    def __init__(
        self,
        button_id: int,
        center: coords.Coords,
        text: str,
        colour: tuple[int, int, int],
        clickable_game_state: game_state.State,
    ):
        super().__init__(
            filename="images/basic_button.png",
            center_x=center.x_coord,
            center_y=center.y_coord,
        )
        self._identifier = button_id
        self.color = colour
        self.clickable_game_state = clickable_game_state

        self.sub_sprites.append(
            arcade.create_text_sprite(
                text,
                start_x=center.x_coord,
                start_y=center.y_coord,
                font_size=32,
                bold=True,
                color=(255, 255, 255),
                anchor_x="center",
                anchor_y="center",
            )
        )

        self._clickable = True

    def is_clickable(self, state: game_state.State) -> bool:
        """
        Check if the button is clickable in the current game state.

        Args:
            game_state (GameState): Current game state.

        Returns:
            bool: whether button is clickable.
        """
        return state is self.clickable_game_state

    def get_id(self) -> int:
        """
        Gets the identifier of the button

        Returns:
            int: enumerated identifier
        """
        return self._identifier
