from board_calculator import BoardCalculator


class GameState:
    """
    A class to represent the state of the game.
    """

    def __init__(self, state: list[list[bool]]) -> None:
        """
        Initializes the GameState with the current state of the board.

        :param state: The current state of the game board.
        """
        self.state = state
        self.board_calculator = BoardCalculator

    def next(self) -> "GameState":
        """
        Calculates the next state of the game and returns a new GameState instance.

        :return: The next state of the game.
        """
        new_state = self.board_calculator(self.state).calc()
        return GameState(new_state)
