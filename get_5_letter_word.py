
def put_5letter_words_in_new_text_file():
    with open("russian_mnemonic_words_5letter.txt", "w", encoding='utf-8') as file:
        for word in get_5letter_words_from_text_file():
            file.write(f'{word}\n')


def get_5letter_words_from_text_file() -> list:
    a = []
    with open("russian_mnemonic_words.txt", "r", encoding='utf-8') as file:
        for line in file:
            if len(line) == 6:
                a.append(line[:-1])
    return a
