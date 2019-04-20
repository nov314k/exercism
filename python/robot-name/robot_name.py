import random
import string


class Robot(object):
    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):
        random.seed()
        name = ''.join(random.sample(string.ascii_uppercase, 2))
        name += ''.join(random.sample(string.digits, 3))
        return name

    def reset(self):
        self.name = self.generate_name()
