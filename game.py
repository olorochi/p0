from random import choices
from enum import StrEnum


class Color(StrEnum):
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    # YELLOW = '\033[33m'
    BLUE = '\033[34m'
    # MAGENTA = '\033[35m'
    # CYAN = '\033[36m'
    WHITE = '\033[37m'
    # DEFAULT = '\033[0m'


class Cell:
    def __init__(self, color):
        self.color = color

    def alive(self):
        return self.color != Color.BLACK


class Game:
    def __init__(self, x, y, life_chance):
        colors = list(Color)
        wgts = [len(colors) - 1 if c == Color.BLACK else life_chance for c in colors]
        self.grid = [[Cell(c) for c in choices(colors, wgts, k=x)] for _ in range(y)]
        # self.update()

    def update(self):
        # starting with all dead means we don't have to kill cells manually
        grid = [[Cell(Color.BLACK) for _ in self.grid[0]] for _ in self.grid]
        from writer import Writer
        Writer.draw(grid)

        for y, row in enumerate(self.grid):
            for x, it in enumerate(row):
                color, n = self.query_cell_neighbors(x, y)
                if (n == 2 and it.alive()):
                    grid[y][x] = it
                elif (n == 3):
                    grid[y][x].color = color

        self.grid = grid

    def query_cell_neighbors(self, x, y):
        colors = dict((c, 0) for c in list(Color))
        colors.pop(Color.BLACK)

        rows = range(max(y - 1, 0), min(y + 2, len(self.grid)))
        for row in rows:
            cols = range(
                    max(x - 1, 0),
                    min(x + 2, len(self.grid[0])),
                    2 if row == y else 1
                    )
            for col in cols:
                it = self.grid[row][col]
                if (it.alive()):
                    colors[it.color] += 1

        n = sum(colors.values())
        color = max(colors, key=colors.get)
        return color, n
