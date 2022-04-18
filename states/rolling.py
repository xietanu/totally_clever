"""RollingGameState"""
from states import game_state
import components


class RollingGameState(game_state.GameState):
    """State for the dice rolling"""

    def start(self):
        """
        Start the dice rolling animations.
        """
        for die in self.game.dice:
            if isinstance(die, components.Die):
                die.start_rolling()

    def end(self):
        """
        Roll the dice finally to get values.
        """
        for die in self.game.dice:
            if isinstance(die, components.Die):
                die.roll()
