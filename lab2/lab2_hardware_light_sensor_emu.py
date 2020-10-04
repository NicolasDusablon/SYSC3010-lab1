import random


def lightinput():
    randnum = randint(1, 10)
    if randnum < 6:
        light = False
    else:
        light = True
    return light
