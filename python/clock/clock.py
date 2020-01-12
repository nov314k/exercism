class Clock:
    def __init__(self, hour, minute):
        while hour < 0:
            hour += 24
        while minute < 0:
            minute += 60
            hour -= 1
        self.hour = hour + minute // 60
        self.minute = minute % 60
        self.hour %= 24 

    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        self.minute = (self.minute + minutes % 60)
        self.hour = (self.hour + (minutes // 60)) % 24

    def __sub__(self, minutes):
        pass
