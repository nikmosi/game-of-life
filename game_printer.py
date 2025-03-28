from game_state import GameState


class GamePrinter:
    """
    A class to print the current state of the game with custom symbols for live and dead cells.
    """

    def __init__(self, game: GameState, live: str, dead: str):
        """
        Initializes the GamePrinter with the game state and symbols for live and dead cells.

        :param game: The current state of the game.
        :param live: The symbol to represent a live cell.
        :param dead: The symbol to represent a dead cell.
        """
        self.state = game.state
        self.live = live
        self.dead = dead

    def print(self):
        """
        Prints the current state of the game.
        """
        game = []

        for row in self.state:
            for is_alive in row:
                game.append(self.live if is_alive else self.dead)
            game.append("\n")

        print("".join(game))
