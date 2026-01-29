class Writer:
    def draw(grid):
        for row in grid:
            for it in row:
                print(it.color, 'X', sep='', end='')
            print()
        print('\033[0m') # reset text style
