from enum import StrEnum
from game import CHUNK_X, CHUNK_Y, Point


class ANSI(StrEnum):
    NO_STYLE = '\033[0m'
    SAVE_POS = '\033[s'
    REST_POS = '\033[u'


class Writer:
    def save_pos():
        print(ANSI.SAVE_POS)

    def draw(game):
        print(ANSI.REST_POS)
        for y in range(game.pos.y, game.pos.y + CHUNK_Y):
            for x in range(game.pos.x, game.pos.x + CHUNK_X):
                div = Point(x // CHUNK_X, y // CHUNK_Y)
                rem = Point(x - div.x, y - div.y)
                print(game[div.x, div.y][Point(rem.x, rem.y)].color, 'X', sep='', end='')
            print()
        print(ANSI.NO_STYLE)
