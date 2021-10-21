from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
jokes = []


def get_jokes(count, is_unique=False):
    """Get a selected count of jokes including words from three lists"""
    joke_prev = []

    for i in range(count):
        joke = list(map(choice, (nouns, adverbs, adjectives)))

        if is_unique:
            while common_word(joke, joke_prev):
                joke = list(map(choice, (nouns, adverbs, adjectives)))

        joke_prev += joke
        jokes.append(' '.join(joke))

    print(jokes)


def common_word(j1, j2):
    return list(set(j1) & set(j2))


get_jokes(5, is_unique=True)
