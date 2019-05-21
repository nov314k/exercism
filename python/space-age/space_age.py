EARTH_YEAR = 31557600

IN_EARTH_YEARS = {
    'Earth': 1,
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132
}


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Mercury'], 2)

    def on_venus(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Venus'], 2)

    def on_earth(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Earth'], 2)

    def on_mars(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Mars'], 2)

    def on_jupiter(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Jupiter'], 2)

    def on_saturn(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Saturn'], 2)

    def on_uranus(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Uranus'], 2)

    def on_neptune(self):
        return round(self.seconds / EARTH_YEAR / IN_EARTH_YEARS['Neptune'], 2)
