from copy import deepcopy
from itertools import product


class BoardCalculator:
    def __init__(self, board: list[list[bool]]) -> None:
        self.board = board
        self.row_len = len(board)

    def calc(self) -> list[list[bool]]:
        new_state = deepcopy(self.board)

        for x, row in enumerate(self.board):
            for y, is_alive in enumerate(row):
                neighbors_count = self._count_neighbors(x, y)
                new_state[x][y] = self._apply_rules(neighbors_count, is_alive)

        return new_state

    def _apply_rules(self, neighbors_count: int, is_alive: bool) -> bool:
        if is_alive:
            return neighbors_count in [2, 3]
        else:
            return neighbors_count == 3

    def _count_neighbors(self, x: int, y: int) -> int:
        count = 0
        for i, j in product([-1, 0, 1], repeat=2):
            if i == j and i == 0:
                continue
            line_len = len(self.board[x])
            row = (i + x + self.row_len) % self.row_len
            ind = (j + y + line_len) % line_len
            count += self.board[row][ind]

        return count
