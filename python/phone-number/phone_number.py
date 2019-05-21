import re


class Phone(object):
    def __init__(self, pn):
        self.number = self.parse_phone_number(pn)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_code = self.number[6:]

    def parse_phone_number(self, pn):
        pn = ''.join(char for char in pn if char.isdigit())
        if len(pn) == 11 and pn.startswith("1"):
            pn = pn[1:]
        if len(pn) != 10:
            raise ValueError("Not a valid telephone number!")
        if re.search("^[2-9]\d{2}[2-9]\d{6}$", pn):
            return pn
        else:
            raise ValueError("Not a valid telephone number!")

    def pretty(self):
        return "({}) {}-{}".format(self.area_code, self.exchange_code,
                                   self.subscriber_code)
