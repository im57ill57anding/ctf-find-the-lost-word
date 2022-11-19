from calculator import *


POSSIBLE = 'qwertyuiopasdfghjklzxcvbnm_'


def go(now, size):
    if len(now) == size:
        if calculate(now) == 315672596408091651900356897796698179520:
            print(now)
            exit(0)
        return

    for i in POSSIBLE:
        go(now + i, size)


if __name__ == '__main__':
    go('', 16)
