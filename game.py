"""
Main game class.
"""
from typing import Optional, Union
import arcade

import colours
import components
import states
import scenes

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Totally Clever"

SCALING = 1


class TotallyClever(arcade.Window):
    """
    Totally Clever game singleton class.
    """
    _instance:Optional[arcade.Window] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TotallyClever, cls).__new__(cls)
            cls._instance.initialized = False
        
        return cls._instance
    
    def __init__(self) -> None:
        if self.initialized:
            return
        
        self.initialized = True
        
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  # type: ignore
        arcade.set_background_color((0, 30, 50))
        self.timer = 0
        self.state = states.RollingGameState(self)
        self._selected_die = None

        self.scenes = {scene_name: arcade.Scene() for scene_name in scenes.SceneNames}

        for layer_name in scenes.MainGameLayers:
            self.scenes[scenes.SceneNames.MAIN_GAME].add_sprite_list(layer_name)

        self.current_scene = self.scenes[scenes.SceneNames.MAIN_GAME]

        self.dice = []
        
        self.roll_button = components.ui.Button(
            button_id=components.ui.ButtonID.ROLL.value,
            center=components.Coords(100, SCREEN_HEIGHT - 100),
            text="Roll!",
            colour=colours.Category.LIBERTY.value,
        )

        self.zones = components.zones.ZoneContainer(components.Coords(300, 0))

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        self.timer = 0

        for layer_name in scenes.MainGameLayers:
            self.scenes[scenes.SceneNames.MAIN_GAME].get_sprite_list(layer_name).clear()

        for y_offset_multiplier, colour in enumerate(colours.Category):
            self.dice.append(
                components.Die(
                    components.Coords(64, 64 + 64 * y_offset_multiplier),
                    colour=colour.value,
                )
            )

    def add_sprites_to_layer(
        self, sprite_or_list: Union[arcade.Sprite, list[arcade.Sprite]], layer: str
    ) -> None:
        """
        Add a single or list of sprites to the named layer in the current scene.

        Args:
            sprites (arcade.Sprite | list[arcade.Sprite]): Single or list of sprites to add
            layer (str): Name of the layer to add the sprites to.
        """
        if isinstance(sprite_or_list, arcade.Sprite):
            sprite_or_list = [sprite_or_list]
        for sprite in sprite_or_list:
            self.current_scene.add_sprite(layer, sprite)

    def on_draw(self):
        """Render the screen."""
        self.clear()
        self.current_scene.draw([layer for layer in scenes.MainGameLayers])

    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        for die in self.dice:
            die.update_animation()

    def on_mouse_press(self, x: float, y: float, button, modifiers) -> None:
        """Called when the user presses a mouse button."""
        position = components.Coords(int(x), int(y))

        if self._selected_die and isinstance(self.state, states.SelectingDieGameState):
            selected_box = None
            for zone in self.zones:
                for box in zone.boxes:
                    if isinstance(
                        box, components.boxes.MarkableBox
                    ) and box.intersects_with_position(position):
                        selected_box = box
                        break
                if selected_box:
                    break

            if selected_box:
                successful_assignment = selected_box.try_mark(self._selected_die)

                if successful_assignment:
                    self._change_state(states.RollingGameState)

        elif isinstance(self.state, states.SelectingDieGameState):
            clicked_die = None

            for die in self.dice:
                if isinstance(die, components.Die) and die.intersects_with_position(
                    position
                ):
                    clicked_die = die
                elif isinstance(die, components.Die):
                    die.reset_selection()

            if clicked_die and clicked_die.on_mouse_press():
                self._selected_die = clicked_die
            else:
                self._selected_die = None

        elif isinstance(
            self.state, states.RollingGameState
        ) and self.roll_button.intersects_with_position(position):
            self._change_state(states.SelectingDieGameState)

    def reset_die_selection(self):
        """Deselect the current die"""
        if self._selected_die:
            self._selected_die.reset_selection()
            self._selected_die = None

    def _change_state(self, new_state: type[states.GameState]) -> None:
        self.state.end()
        self.state = new_state(self)
        self.state.start()
