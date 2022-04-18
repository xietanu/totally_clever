"""GameState"""


class GameState:
    """An object describing the current state of the game."""

    def __init__(self, parent_game) -> None:
        self.game = parent_game

    def start(self):
        """
        Actions to run when the state is initiated.

        By default, no action taken
        """

    def end(self):
        """
        Actions to run when the state is ended.

        By default, no action taken
        """
