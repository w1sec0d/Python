import math


def distance(x1, y1, x2, y2):
    return math.sqrt(abs(x1-x2)**2 + abs(y1-y2) ** 2)


print(distance(4, 0, 6, 6))
