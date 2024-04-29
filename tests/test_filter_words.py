from unittest import TestCase

from classes import LetterInWord, LetterOutWord
from filter_words import find_words_with_leters_with_right_pos, find_words_without_letters_with_wrong_pos, \
    find_words_without_leters, find_words_with_leters, get_filtered_words


class FilterWordsTestCase(TestCase):
    def setUp(self):
        self.words = ['обувь', 'объём', 'овраг', 'овсюг', 'огонь', 'огрех', 'озеро', 'озимь', 'озноб', 'ойрот', 'океан',
                      'окись', 'оклик', 'окрас', 'окрик', 'окрол', 'октет', 'окунь']
        self.letters_in_word = LetterInWord()
        self.letters_out_word = LetterOutWord()
        self.letters_in_word.letters = ['о', 'к', 'и']
        self.letters_in_word.letters_with_right_pos = ['о1', 'к5']
        self.letters_in_word.letters_with_wrong_pos = ['и2', 'к4']
        self.letters_out_word.letters = ['в', 'с', 'м']

    def test_find_words_with_leters_with_right_pos(self):
        self.assertEqual(find_words_with_leters_with_right_pos(self.words, self.letters_in_word.letters_with_right_pos),
                         ['оклик', 'окрик'])

    def test_find_words_without_letters_with_wrong_pos(self):
        self.assertEqual(
            len(find_words_without_letters_with_wrong_pos(self.words, self.letters_in_word.letters_with_wrong_pos)),
            18)

    def test_find_words_without_leters(self):
        self.assertEqual(find_words_without_leters(self.words, self.letters_out_word.letters),
                         ['огонь', 'огрех', 'озеро', 'озноб', 'ойрот', 'океан', 'оклик', 'окрик', 'окрол', 'октет',
                          'окунь'])

    def test_find_words_with_leters(self):
        self.assertEqual(find_words_with_leters(self.words, self.letters_in_word.letters), ['окись', 'оклик', 'окрик'])

    def test_get_filtered_words(self):
        self.assertEqual(get_filtered_words(self.words, self.letters_in_word,self.letters_out_word), ['оклик', 'окрик'])
