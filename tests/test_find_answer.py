from unittest import TestCase
from unittest.mock import patch

from find_answer import get_random_word, get_all_5_letter_words, find_answer


class FindAnswerTestCase(TestCase):
    def setUp(self):
        self.words = ['обувь', 'объём', 'овраг', 'овсюг', 'огонь', 'огрех', 'озеро', 'озимь', 'озноб', 'ойрот', 'океан',
                      'окись', 'оклик', 'окрас', 'окрик', 'окрол', 'октет', 'окунь']

    @patch('random.randrange')
    def test_get_random_word(self, mock_randrange):
        mock_randrange.return_value = 6
        self.assertEqual(get_random_word(self.words), 'озеро')

    def test_get_all_5_letter_words(self):
        self.assertEqual(len(get_all_5_letter_words()), 2076)
