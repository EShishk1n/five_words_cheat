from classes import LetterInWord, LetterOutWord


def get_filtered_words(all_words: list, letters_in_word: LetterInWord, letters_out_word: LetterOutWord) -> list:

    words_with_letters = find_words_with_leters(words=all_words, letters_in_word=letters_in_word.letters)

    words_without_letters = find_words_without_leters(words=words_with_letters,
                                                      letters_out_word=letters_out_word.letters)

    words_without_letters_with_wrong_pos = (
        find_words_without_letters_with_wrong_pos(words=words_without_letters,
                                                  letters_with_wrong_pos=letters_in_word.letters_with_wrong_pos))

    words_with_letters_with_right_pos = (
        find_words_with_leters_with_right_pos(words=words_without_letters_with_wrong_pos,
                                              letters_with_right_pos=letters_in_word.letters_with_right_pos))

    result = words_with_letters_with_right_pos

    return result


def find_words_with_leters(words: list, letters_in_word) -> list:
    result = []
    letters_in_word = set(letters_in_word)

    for word in words:
        if letters_in_word.issubset(set(word)):
            result.append(word)

    return result


def find_words_without_leters(words: list, letters_out_word) -> list:
    result = []
    letters_out_word = set(letters_out_word)

    for word in words:
        if letters_out_word.isdisjoint(set(word)):
            result.append(word)

    return result


def find_words_without_letters_with_wrong_pos(words: list, letters_with_wrong_pos) -> list:
    result = []
    letters_with_wrong_pos = set(letters_with_wrong_pos)
    if words:
        for word in words:
            letters_in_word_with_pos = []
            for i in range(5):
                letters_in_word_with_pos.append(str(word[i]) + str(i+1))
            if letters_with_wrong_pos.isdisjoint(set(letters_in_word_with_pos)):
                result.append(word)

    return result


def find_words_with_leters_with_right_pos(words: list, letters_with_right_pos: list) -> list:
    result = []
    if letters_with_right_pos != ['']:
        letters_with_right_pos = set(letters_with_right_pos)
    else:
        letters_with_right_pos = set()
    if words:
        for word in words:
            letters_in_word_with_pos = []
            for i in range(5):
                letters_in_word_with_pos.append(str(word[i]) + str(i+1))
            if letters_with_right_pos.issubset(set(letters_in_word_with_pos)):
                result.append(word)

    return result
