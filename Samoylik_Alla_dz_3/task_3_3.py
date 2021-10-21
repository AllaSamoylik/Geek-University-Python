name_dict = {}


def thesaurus(*args):
    for name in args:
        name_dict.setdefault(name[:1], []).append(name)
    print(name_dict)


thesaurus('Иван', 'Мария', 'Петр', 'Илья')
