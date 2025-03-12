from game_printer import GamePrinter
from game_state import GameState


def main():
    start_state = [[False for _ in range(10)] for _ in range(10)]
    start_state[6][3] = True
    start_state[7][3] = True
    start_state[7][2] = True
    start_state[8][3] = True
    start_state[8][4] = True
    game = GameState(state=start_state)
    for _ in range(10_000):
        GamePrinter(game, "#", ".").print()
        input("")
        game = game.next()


if __name__ == "__main__":
    main()
