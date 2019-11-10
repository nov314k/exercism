signals = ['wink', 'double blink', 'close your eyes', 'jump']


def commands(number):
    code = [signals[i] for i in range(len(signals))
            if (number >> i) % 2 == 1]
    return code if number < 16 else list(reversed(code))
