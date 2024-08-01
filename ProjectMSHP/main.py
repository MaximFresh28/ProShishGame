"""Файл для запуска игры."""

from GameEngine import Game

def main() -> None:
    """
    Switch on our game.
    """
    game = Game()
    game.run()



if __name__ == "__main__":
    main()
