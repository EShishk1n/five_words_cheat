from unittest import TestCase

from classes import LetterInWord, LetterOutWord, form_letter_objects


class LetterInWordTestCase(TestCase):

    def setUp(self):
        self.letters_in_word = LetterInWord()
        self.letters_from_keyboard = {'in_word_wrong_pos': ['a4', 'd2'],
                                      'in_word_right_pos': ['k1'],
                                      'out_word': ['g', 'i', 'l']}
        self.no_letters_from_keyboard = {'in_word_wrong_pos': [''],
                                         'in_word_right_pos': [''],
                                         'out_word': ['']}

    def test_add_letters(self):
        self.letters_in_word.add_letters(self.letters_from_keyboard)
        self.letters_in_word.add_letters(self.no_letters_from_keyboard)
        self.assertEqual(self.letters_in_word.letters, ['a', 'd', 'k'])

    def test_add_letters_with_wrong_pos(self):
        self.letters_in_word.add_letters_with_wrong_pos(self.letters_from_keyboard)
        self.letters_in_word.add_letters_with_wrong_pos(self.no_letters_from_keyboard)
        self.assertEqual(self.letters_in_word.letters_with_wrong_pos, ['a4', 'd2'])

    def test_add_letters_with_right_pos(self):
        self.letters_in_word.add_letters_with_right_pos(self.letters_from_keyboard)
        self.letters_in_word.add_letters_with_right_pos(self.no_letters_from_keyboard)
        self.assertEqual(self.letters_in_word.letters_with_right_pos, ['k1'])


class LetterOutWordTestCase(TestCase):
    def setUp(self):
        self.letters_out_word = LetterOutWord()
        self.letters_in_word = ['a', 'd', 'k']
        self.letters_from_keyboard = {'in_word_wrong_pos': ['a4', 'd2'],
                                      'in_word_right_pos': ['k1'],
                                      'out_word': ['g', 'i', 'l']}
        self.no_letters_from_keyboard = {'in_word_wrong_pos': [''],
                                         'in_word_right_pos': [''],
                                         'out_word': ['']}

    def test_add_letters(self):
        self.letters_out_word.add_letters(self.no_letters_from_keyboard, self.letters_in_word)
        self.letters_out_word.add_letters(self.letters_from_keyboard, self.letters_in_word)
        self.assertEqual(self.letters_out_word.letters, ['g', 'i', 'l'])


class FormLetterObjectsTestCase(TestCase):
    def setUp(self):
        self.letters_from_keyboard = {'in_word_wrong_pos': ['a4', 'd2'],
                                      'in_word_right_pos': ['k1'],
                                      'out_word': ['g', 'i', 'l']}
        self.letters_in_word = LetterInWord()
        self.letters_out_word = LetterOutWord()

    def test_form_letter_objects(self):
        form_letter_objects(self.letters_in_word, self.letters_out_word, self.letters_from_keyboard)
        self.assertEqual(self.letters_in_word.letters, ['a', 'd', 'k'])
        self.assertEqual(self.letters_in_word.letters_with_wrong_pos, ['a4', 'd2'])
        self.assertEqual(self.letters_out_word.letters, ['g', 'i', 'l'])
