def equilateral(sides):
    return valid(sides) \
           and all(sides[0] == s for s in sides)


def isosceles(sides):
    return valid(sides) \
           and any(a == b
                   for a, b
                   in zip(sorted(sides), sorted(sides[1::])))


def scalene(sides):
    return valid(sides) \
           and any(a != b
                   for a, b
                   in zip(sorted(sides), sorted(sides[1::])))


def valid(sides):
    return all(s > 0 for s in sides) \
           and sum(sorted(sides)[:2]) >= sorted(sides)[2]
