def merge_letter_lists_to_dict() -> dict:

    letters = take_letters_from_keyboard()

    result = {'in_word_wrong_pos': take_letters_from_input(letters, 'in_word_wrong_pos'),
              'in_word_right_pos': take_letters_from_input(letters, 'in_word_right_pos'),
              'out_word': take_letters_from_input(letters, 'out_word')}

    return result


def take_letters_from_keyboard() -> list:
    letters = input(
        'Введите буквы через запятую (буквапозиция которые стоят не на своих местах, '
        'буквапозиция которые стоят на своих местах, '
        'буквы которых нет в слове) -> \n пример а2 г5, у8, х л с: ')

    return letters.split(', ')


def take_letters_from_input(letters: list, letters_type: str) -> list:

    match letters_type:
        case 'in_word_wrong_pos':
            return letters[0].split(' ')
        case 'in_word_right_pos':
            return letters[1].split(' ')
        case 'out_word':
            return letters[2].split(' ')
