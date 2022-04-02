"""
Main game class.
"""
import arcade

import colours
import components
import game_state
import sprites

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Totally Clever"

SCALING = 1


class TotallyClever(arcade.Window):
    """
    Totally Clever game class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # type: ignore
        arcade.set_background_color((0, 30, 50))
        self.timer = 0

        self.zones = sprites.MultiSpriteList(use_spatial_hash=True)
        self.dice = sprites.MultiSpriteList()
        self.buttons = sprites.MultiSpriteList(use_spatial_hash=True)

        self.state = game_state.State.ROLLING

        self._selected_die = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.timer = 0

        self.zones = sprites.MultiSpriteList(use_spatial_hash=True)
        self.dice = sprites.MultiSpriteList()
        self.buttons = sprites.MultiSpriteList(use_spatial_hash=True)

        at_least_category = components.zones.AtLeast(
            sprites.filepaths.ZoneSprite.SHORT.value,
            colours.Category.SUNGLOW.value,
            components.Coords(300, 0),
        )
        self.zones.append(at_least_category)

        at_least_category.add_decorative_sprite(
            "images/arrow_icon.png", components.Coords(30, 50), apply_color=True
        )

        for x_offset, min_value in enumerate(list(range(1, 6)) + list(range(1, 7))):
            at_least_category.add_box(
                components.boxes.MinValueBox(min_value),
                components.Coords(70 + 40 * x_offset, 50),
            )

        for y_offset_multiplier, colour in enumerate(colours.Category):
            self.dice.append(
                components.Die(
                    components.Coords(64, 64 + 64 * y_offset_multiplier),
                    colour=colour.value,
                )
            )

        self.buttons.append(
            components.ui.Button(
                button_id=components.ui.ButtonID.ROLL.value,
                center=components.Coords(100, SCREEN_HEIGHT - 100),
                text="Roll!",
                colour=colours.Category.LIBERTY.value,
            )
        )

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.zones.draw()
        self.dice.draw()
        self.buttons.draw()

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        for die in self.dice:
            die.update_animation()

    def on_mouse_press(self, x: float, y: float, button, modifiers) -> None:
        """Called when the user presses a mouse button."""
        clicked_items = (
            arcade.get_sprites_at_point((x, y), self.dice)
            + arcade.get_sprites_at_point((x, y), self.buttons)
            + arcade.get_sprites_at_point((x, y), self.zones)
        )

        if not clicked_items:
            return

        clicked_item = clicked_items[0]

        if (
            isinstance(clicked_item, components.zones.Zone)
            and self._selected_die
            and clicked_item.color == self._selected_die.color
        ):
            clicked_item.on_mouse_press(
                components.Coords(int(x), int(y)), value=self._selected_die.side
            )

        elif (
            isinstance(clicked_item, components.Die)
            and self.state == game_state.State.SELECTING_DIE
        ):
            if clicked_item.on_mouse_press():
                self._selected_die = clicked_item
            else:
                self._selected_die = None

        elif isinstance(clicked_item, components.ui.Button):
            if (
                clicked_item.identifier == components.ui.ButtonID.ROLL.value
                and self.state == game_state.State.ROLLING
            ):
                for die in self.dice:
                    if isinstance(die, components.Die):
                        die.roll()
                self.state = game_state.State.SELECTING_DIE
