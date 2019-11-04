import random
from itertools import cycle
from string import ascii_lowercase
from time import time


class Cipher(object):
    def __init__(self, key=None):
        if key is None:
            random.seed(time())
            key = ''.join(random.choice(ascii_lowercase)
                          for i in range(100))
        self.key = key

    def encode(self, text):
        return ''.join(
            chr(
                ((ord(letter) - 2 * ord('a') + ord(shift)) % 26)
                + ord('a')
            )
            for letter, shift in zip(text, cycle(self.key))
        )

    def decode(self, text):
        return ''.join(
            chr(((ord(letter) - ord(shift)) % 26) + ord('a'))
            for letter, shift in zip(text, cycle(self.key))
        )
