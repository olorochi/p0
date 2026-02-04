import time
import os
from game import Game
from writer import Writer


DELAY = 0.5

game = Game()
Writer.draw(game)
os.system('cls' if os.name == 'nt' else 'clear')

while (True):
    time.sleep(DELAY)
    game.pos.x += 1
    game.update()
    Writer.draw(game)
