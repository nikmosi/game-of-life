from board_calculator import BoardCalculator


class GameState:
    def __init__(self, state: list[list[bool]]) -> None:
        self.state = state
        self.board_calculator = BoardCalculator

    def next(self) -> "GameState":
        new_state = self.board_calculator(self.state).calc()
        return GameState(new_state)
