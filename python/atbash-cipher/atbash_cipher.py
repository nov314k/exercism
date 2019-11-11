from string import ascii_lowercase

BLOCK_SIZE = 5
MAPPING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def endec(text):
    return ''.join([c for c in text if c.isalnum()]).lower().translate(MAPPING)


def encode(plain_text):
    encoded_string = endec(plain_text)
    return " ".join([encoded_string[i:i + BLOCK_SIZE]
                     for i in range(0, len(encoded_string), BLOCK_SIZE)])


def decode(ciphered_text):
    return endec(ciphered_text)
