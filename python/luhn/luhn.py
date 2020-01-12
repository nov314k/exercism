class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def double_except_nine(self, number):
        doubled_number = 2 * number
        if doubled_number > 9:
            doubled_number -= 9
        return doubled_number

    def valid(self):
        self.card_num = self.card_num.replace(" ", "")
        if not self.card_num.isdigit() or len(self.card_num) < 2:
            return False
        numbers = [int(num) for num in self.card_num]
        # For even-length card_num's, even-index digits are doubled
        # For  odd-length card_num's,  odd-index digits are doubled
        doubled_digits_sum = sum(
            [self.double_except_nine(num) for num in numbers[-2::-2]])
        normal_digits_sum = sum(numbers[-1::-2])
        all_digits_sum = doubled_digits_sum + normal_digits_sum
        return all_digits_sum % 10 == 0
