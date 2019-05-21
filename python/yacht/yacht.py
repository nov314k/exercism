from collections import Counter

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 10
FOUR_OF_A_KIND = 11
CHOICE = 12
STRAIGHT = 30
BIG_STRAIGHT = 31
LITTLE_STRAIGHT = 32
YACHT = 50


def score(dice, category):
    score = 0
    counter = Counter(dice)
    if category < 10:
        score = sum(f for f in dice if f == category)
    if category == YACHT:
        number, count = counter.most_common()[0]
        if count == 5:
            score = YACHT
    if category == FOUR_OF_A_KIND:
        number, count = counter.most_common()[0]
        if count >= 4:
            score = 4 * number
    if category == FULL_HOUSE:
        if set(counter.values()) == {3, 2}:
            score = sum(dice)
    if category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            score = STRAIGHT
    if category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            score = STRAIGHT
    if category == CHOICE:
        score = sum(dice)
    return score
