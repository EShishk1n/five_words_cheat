class LetterInWord:

    def __init__(self):
        self.letters = []
        self.letters_with_wrong_pos = []
        self.letters_with_right_pos = []

    def add_letters(self, letters_from_keyboard: dict):
        letters = letters_from_keyboard['in_word_wrong_pos'] + letters_from_keyboard['in_word_right_pos']

        for letter in letters:
            if letter != '':
                self.letters.append(letter[0])

    def add_letters_with_wrong_pos(self, letters_from_keyboard: dict):
        letters_with_wrong_pos = letters_from_keyboard['in_word_wrong_pos']
        if letters_with_wrong_pos != ['']:
            self.letters_with_wrong_pos += letters_with_wrong_pos

    def add_letters_with_right_pos(self, letters_from_keyboard: dict):
        letters_with_right_pos = letters_from_keyboard['in_word_right_pos']
        if letters_with_right_pos != ['']:
            self.letters_with_right_pos += letters_with_right_pos


class LetterOutWord:

    def __init__(self):
        self.letters = []

    def add_letters(self, letters_from_keyboard: dict, letters_in_word: list):
        letters = letters_from_keyboard['out_word']
        if letters != ['']:
            if set(letters).isdisjoint(set(letters_in_word)):
                self.letters += letters


def form_letter_objects(letters_in_word: LetterInWord, letters_out_word: LetterOutWord,
                        letters_from_keyboard: dict) -> None:
    letters_in_word.add_letters(letters_from_keyboard)
    letters_in_word.add_letters_with_wrong_pos(letters_from_keyboard)
    letters_in_word.add_letters_with_right_pos(letters_from_keyboard)
    letters_out_word.add_letters(letters_from_keyboard, letters_in_word.letters)
