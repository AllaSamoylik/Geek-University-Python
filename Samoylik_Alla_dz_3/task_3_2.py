eng_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(numb_eng):
    if numb_eng.istitle():
        print(eng_dict.get(numb_eng.lower()).capitalize())
    else:
        print(eng_dict.get(numb_eng))


num_translate_adv(input('Введите число 0 до 10 (прописью): '))
