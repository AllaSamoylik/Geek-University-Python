from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Фёдор', 'Станислав']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

pairs = list(zip(tutors, klasses) if len(tutors) <= len(klasses) else zip_longest(tutors, klasses))

result = ((pair[0], pair[1]) for pair in pairs)
print(type(result))
print('-' * 20)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
