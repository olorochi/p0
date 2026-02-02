import time
from game import Game
from writer import Writer


DELAY = 0.5

game = Game()
Writer.save_pos()
Writer.draw(game)

while (True):
    time.sleep(DELAY)
    game.update()
    Writer.draw(game)
