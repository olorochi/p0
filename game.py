import random
from enum import StrEnum
from keydefaultdict import keydefaultdict
from copy import copy


CHUNK_Y = 40
CHUNK_X = 80
LIFE_CHANCE = 0.2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Color(StrEnum):
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    # YELLOW = '\033[33m'
    BLUE = '\033[34m'
    # MAGENTA = '\033[35m'
    # CYAN = '\033[36m'
    WHITE = '\033[37m'


class Cell:
    def __init__(self, color):
        self.color = color

    def alive(self):
        return self.color != Color.BLACK


class Chunk:
    def __init__(self, parent, offset):
        colors = list(Color)
        wgts = [len(colors) - 1 if c == Color.BLACK else LIFE_CHANCE for c in colors]
        self.grid = [[Cell(c) for c in random.choices(colors, wgts, k=CHUNK_X)] for _ in range(CHUNK_Y)]
        self.__update(parent, offset, False)

    def __getitem__(self, pos):
        return self.grid[pos.y][pos.x]

    def __update(self, parent, offset, spill):
        # starting with all dead means we don't have to kill cells manually
        grid = [[Cell(Color.BLACK) for _ in self.grid[0]] for _ in self.grid]

        for y, row in enumerate(self.grid):
            for x, it in enumerate(row):
                color, n = self.query_neighbors(parent, x + offset.x, y + offset.y, spill)
                if (n == 2 and it.alive()):
                    grid[y][x] = it
                elif (n == 3):
                    grid[y][x].color = color

        self.grid = grid

    def query_neighbors(self, parent, x, y, spill):
        colors = dict((c, 0) for c in list(Color))

        # should probably be rewritten
        if spill:
            for row in range(y - 1, y + 2):
                for col in range(x - 1, x + 2, 2 if y == row else 1):
                    it = parent[Point(col, row)]
                    if (it.alive()):
                        colors[it.color] += 1
        else:
            x %= CHUNK_X
            y %= CHUNK_Y
            for row in range(max(y - 1, 0), min(y + 2, CHUNK_Y)):
                for col in range(max(x - 1, 0), min(x + 2, CHUNK_X), 2 if y == row else 1):
                    it = self[Point(col, row)]
                    if (it.alive()):
                        colors[it.color] += 1

        n = sum(colors.values())
        high = max(colors.values())
        color = random.choice([c for c, v in colors.items() if v == high])
        return color, n

    def get_updated(self, parent, offset):
        out = copy(self)
        out.__update(parent, offset, True)
        return out

    def in_bounds(self, pos):
        return pos.x >= 0 and pos.x < CHUNK_X and pos.y >= 0 and pos.y < CHUNK_Y


class Game:
    def __init__(self):
        self.pos = Point(CHUNK_X // 2, CHUNK_Y // 2)
        self.grid = keydefaultdict(lambda k: Chunk(self, Point(k[0], k[1])))
        self.update()

    def __getitem__(self, pos):
        div = Point(pos.x // CHUNK_X, pos.y // CHUNK_Y)
        rem = Point(pos.x - div.x * CHUNK_X, pos.y - div.y * CHUNK_Y)
        return self.grid[div.x, div.y][rem]

    def update(self):
        grid = {}

        chunk = Point(self.pos.x // CHUNK_X, self.pos.y // CHUNK_Y)
        for y in range(chunk.y - 1, chunk.y + 2):
            for x in range(chunk.x - 1, chunk.x + 2):
                grid[x, y] = self.grid[x, y].get_updated(self, Point(x, y))

        self.grid.update(grid)
