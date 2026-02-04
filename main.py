import time
import os
import threading
from game import Game, Point
from writer import Writer
from queue import Queue
from enum import Enum, auto
from getch import getch


DELAY = 0.5


class EventType(Enum):
    INPUT = auto(),
    UPDATE = auto()


class Event:
    def __init__(self, evtype):
        self.type = evtype


class InputEvent(Event):
    def __init__(self, vec):
        Event.__init__(self, EventType.INPUT)
        self.vec = vec


def input_thr():
    while True:
        c = getch()
        if c == 'h':
            pt = Point(-1, 0)
        elif c == 'j':
            pt = Point(0, 1)
        elif c == 'k':
            pt = Point(0, -1)
        elif c == 'l':
            pt = Point(1, 0)
        else:
            return

        evs.put(InputEvent(pt))


def update_thr():
    while True:
        evs.put(Event(EventType.UPDATE))
        time.sleep(DELAY)


os.system('cls' if os.name == 'nt' else 'clear')
game = Game()
evs = Queue()
for fn in [input_thr, update_thr]:
    thr = threading.Thread(target=fn)
    thr.start()

while True:
    ev = evs.get()
    if (ev.type == EventType.INPUT):
        game.pos += ev.vec

    game.update()
    Writer.draw(game)
