import random

from classes import LetterInWord, LetterOutWord, form_letter_objects
from filter_words import get_filtered_words
from take_letters_from_keyboard import merge_letter_lists_to_dict


def find_answer():
    all_words = get_all_5_letter_words()

    print(get_random_word(get_all_5_letter_words()))

    letters_in_word = LetterInWord()
    letters_out_word = LetterOutWord()

    result_words = []

    for i in range(5):
        letters_from_keyboard = merge_letter_lists_to_dict()

        form_letter_objects(letters_in_word, letters_out_word, letters_from_keyboard)

        result_words = get_filtered_words(all_words, letters_in_word, letters_out_word)

        if len(result_words) >= 1:
            print(result_words[random.randrange(len(result_words))])
        else:
            print('нет таких слов')
            break

    return result_words


def get_all_5_letter_words() -> list:
    all_words = []
    with open("C:/projects/five_letters/russian-words/russian_mnemonic_words_5letter.txt", "r", encoding='utf-8') as file:
        for word in file:
            all_words.append(word[:-1])

    return all_words


def get_random_word(all_words: list) -> None:
    return all_words[random.randrange(len(all_words))]


if __name__ == '__main__':
    find_answer()
