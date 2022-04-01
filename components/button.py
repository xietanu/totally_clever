"""Button class"""
from arcade import create_text_sprite
from abstracts.coords import Coords
from abstracts.multi_sprite import MultiSprite


class Button(MultiSprite):
    """Class for clickable button to trigger behaviour"""
    def __init__(
        self,
        button_id: str,
        center: Coords,
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

        self.sub_sprites.append(
            create_text_sprite(
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
