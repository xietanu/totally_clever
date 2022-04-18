"""SelectingDieGameState"""
from states import game_state


class SelectingDieGameState(
    game_state.GameState
):  # pylint: disable=too-few-public-methods
    """State for the selecting and assigning dice"""

    def end(self):
        """
        Deselect dice once selected.
        """
        self.game.reset_die_selection()
