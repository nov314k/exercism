MAPPING_FOR_ENCODING = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n',
    'n': 'm',
    'o': 'l',
    'p': 'k',
    'q': 'j',
    'r': 'i',
    's': 'h',
    't': 'g',
    'u': 'f',
    'v': 'e',
    'w': 'd',
    'x': 'c',
    'y': 'b',
    'z': 'a'
}

BLOCK_SIZE = 5
MAPPING_FOR_DECODING = {v: k for k, v in MAPPING_FOR_ENCODING.items()}


def encode(plain_text):
    encoded_string = ""
    for char in plain_text:
        if char.isalpha():
            encoded_string += MAPPING_FOR_ENCODING[char.lower()]
        elif char.isnumeric():
            encoded_string += char
    return " ".join([encoded_string[i:i + BLOCK_SIZE]
                     for i in range(0, len(encoded_string), BLOCK_SIZE)])


def decode(ciphered_text):
    decoded_string = ""
    for char in ciphered_text:
        if char.isalpha():
            decoded_string += MAPPING_FOR_DECODING[char]
        elif char.isnumeric():
            decoded_string += char
    return decoded_string
