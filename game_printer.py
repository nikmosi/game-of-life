from game_state import GameState


class GamePrinter:
    def __init__(self, game: GameState, live: str, dead: str):
        self.state = game.state
        self.live = live
        self.dead = dead

    def print(self):
        game = []

        for row in self.state:
            for is_alive in row:
                game.append(self.live if is_alive else self.dead)
            game.append("\n")

        print("".join(game))
