import os


# Based on answers in: https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
def _find_getch():
    if os.name == "nt":
        import msvcrt
        return msvcrt.getch

    import sys
    import tty

    def __getch_unix():
        fd = sys.stdin.fileno()
        tty.setcbreak(fd)
        ch = sys.stdin.read(1)
        return ch

    return __getch_unix


getch = _find_getch()
