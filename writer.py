from enum import StrEnum
from game import CHUNK_X, CHUNK_Y, Point


class ANSI(StrEnum):
    NO_STYLE = '\033[0m'
    HOME = '\033[H'


class Writer:
    @staticmethod
    def draw(game):
        print(ANSI.HOME, end='')
        for y in range(game.pos.y, game.pos.y + CHUNK_Y):
            for x in range(game.pos.x, game.pos.x + CHUNK_X):
                print(game[Point(x, y)].color, 'X', sep='', end='')
            print()
        print(ANSI.NO_STYLE, end='')
