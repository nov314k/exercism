def raindrops(number):
    factors = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    sound = [f[1] for f in factors if number % f[0] == 0 and number != 1]
    if sound:
        return "".join(sound)
    else:
        return str(number)
