def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    elif hey_bob.isupper():
        if '?' in hey_bob:
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob.strip()[-1] == '?':
        return "Sure."
    else:
        return "Whatever."
