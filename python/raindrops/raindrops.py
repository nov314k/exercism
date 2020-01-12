DROPS = (
   ('Pling', 3),
   ('Plang', 5),
   ('Plong', 7),
)

def raindrops(number):
    sound = "".join(s for s, n in DROPS if not number % n)
    return str(sound or number)
