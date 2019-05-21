# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = "".join('_' for i in range(0, len(self.word)))

    def guess(self, char):
        if self.status == STATUS_ONGOING:
            if char in self.word and char not in self.masked_word:
                masked_word_list = list(self.masked_word)
                for i in range(0, len(self.word)):
                    if char == self.word[i]:
                        masked_word_list[i] = char
                self.masked_word = "".join(masked_word_list)
                if '_' not in self.masked_word:
                    self.status = STATUS_WIN
            else:
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
        else:
            raise ValueError("Current game is not ongoing!")

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status
