from math import sqrt

POINTS_TABLE = {
    1: 10,
    5: 5,
    10: 1,
    1000: 0
}


def score(x, y):
    for r, score in POINTS_TABLE.items():
        if sqrt(x**2 + y**2) <= r:
            return score
