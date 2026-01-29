from game import Color


class Writer:
    def draw(grid):
        for row in grid:
            for it in row:
                print('X' if it.color == Color.WHITE else ' ', sep='', end='')
            print()
        print('\033[0m')
