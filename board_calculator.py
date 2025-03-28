from itertools import product


class BoardCalculator:
    """
    A class to calculate the next state of the game board.
    """

    def __init__(self, board: list[list[bool]]) -> None:
        """
        Initializes the BoardCalculator with the current state of the board.

        :param board: The current state of the game board.
        """
        self.board = board
        self.row_len = len(board)
        self.col_len = len(board[0]) if self.row_len > 0 else 0

    def calc(self) -> list[list[bool]]:
        """
        Calculates the next state of the board based on the current state.

        :return: The next state of the board.
        """
        new_state = [
            [
                self._apply_rules(self._count_neighbors(x, y), cell)
                for y, cell in enumerate(row)
            ]
            for x, row in enumerate(self.board)
        ]
        return new_state

    def _apply_rules(self, neighbors_count: int, is_alive: bool) -> bool:
        """
        Applies the rules of the game to determine if a cell should be alive or dead.

        :param neighbors_count: The number of live neighbors around the cell.
        :param is_alive: The current state of the cell (alive or dead).
        :return: The new state of the cell (alive or dead).
        """
        if is_alive:
            return neighbors_count in [2, 3]
        return neighbors_count == 3

    def _count_neighbors(self, x: int, y: int) -> int:
        """
        Counts the number of live neighbors around a given cell.

        :param x: The x-coordinate of the cell.
        :param y: The y-coordinate of the cell.
        :return: The number of live neighbors around the cell.
        """
        count = 0
        for i, j in product([-1, 0, 1], repeat=2):
            if i == 0 and j == 0:
                continue
            row = (x + i) % self.row_len
            col = (y + j) % self.col_len
            count += self.board[row][col]
        return count
