import time
from game import Game
from writer import Writer


GRID_HEIGHT = 40
GRID_WIDTH = 80
LIFE_CHANCE = 0.3

game = Game(GRID_WIDTH, GRID_HEIGHT, LIFE_CHANCE)
Writer.draw(game.grid)

while (True):
    time.sleep(1)
    game.update()
    Writer.draw(game.grid)
