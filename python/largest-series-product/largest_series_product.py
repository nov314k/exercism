from functools import reduce
from operator import mul


def segments(series, length):
    segment = [int(digit) for digit in series]
    if not 1 <= length <= len(segment):
        raise ValueError("Invalid slice length")
    return [segment[i:i + length]
            for i in range(len(segment) - length + 1)]


def largest_product(series, length):
    if length == 0:
        return 1
    return max(reduce(mul, segment) for segment in segments(series, length))
