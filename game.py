from random import choice
from enum import StrEnum


class Color(StrEnum):
    BLACK = '\033[30m'
    # RED = '\033[31m'
    # GREEN = '\033[32m'
    # YELLOW = '\033[33m'
    # BLUE = '\033[34m'
    # MAGENTA = '\033[35m'
    # CYAN = '\033[36m'
    WHITE = '\033[37m'
    # DEFAULT = '\033[0m'


class Cell:
    def __init__(self, color):
        self.color = color

    def alive(self):
        return self.color != Color.BLACK

    def die(self):
        self.color = Color.BLACK

    def spawn(self):
        self.color = Color.WHITE


class Game:
    def __init__(self, x, y):
        colors = list(Color)
        self.grid = [
                [Cell(choice(colors)) for _ in range(x)] for _ in range(y)
            ]
        # update()

    def update(self):
        kill = list()
        spawn = list()

        for y, row in enumerate(self.grid):
            for x, it in enumerate(row):
                n = self.count_cell_neighbors(x, y)
                if (n == 2):
                    pass
                elif (n == 3):
                    spawn.append(it)
                else:
                    kill.append(it)

        for it in kill:
            it.die()

        for it in spawn:
            it.spawn()

    def count_cell_neighbors(self, x, y):
        n = 0
        rows = range(max(y - 1, 0), min(y + 2, len(self.grid)))
        for row in rows:
            cols = range(
                    max(x - 1, 0),
                    min(x + 2, len(self.grid[0])),
                    2 if row == y else 1
                    )
            for col in cols:
                if (self.grid[row][col].alive()):
                    n += 1
        return n
