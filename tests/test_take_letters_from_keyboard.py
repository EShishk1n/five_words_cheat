from unittest import TestCase
from unittest.mock import patch

from take_letters_from_keyboard import take_letters_from_input, take_letters_from_keyboard, merge_letter_lists_to_dict


class TakeLettersFromKeyboardTestCase(TestCase):

    def setUp(self):
        self.lists = ['a4 d2', 'k1', 'g i l']

    def test_take_letters_out_word(self):
        self.assertEqual(take_letters_from_input(self.lists, 'in_word_wrong_pos'), ['a4', 'd2'])
        self.assertEqual(take_letters_from_input(self.lists, 'in_word_right_pos'), ['k1'])
        self.assertEqual(take_letters_from_input(self.lists, 'out_word'), ['g', 'i', 'l'])

    @patch('builtins.input')
    def test_take_letters_from_keyboard(self, mock_input):
        mock_input.return_value = 'a4 d2, k1, g i l'
        self.assertEqual(take_letters_from_keyboard(), self.lists)

    @patch('take_letters_from_keyboard.take_letters_from_keyboard')
    def test_merge_letter_lists_to_dict(self, mock_take_letters_from_keyboard):
        mock_take_letters_from_keyboard.return_value = self.lists
        self.assertEqual(merge_letter_lists_to_dict(), {'in_word_wrong_pos': ['a4', 'd2'],
                                                        'in_word_right_pos': ['k1'],
                                                        'out_word': ['g', 'i', 'l']})
