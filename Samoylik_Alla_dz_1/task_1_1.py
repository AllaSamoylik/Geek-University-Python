duration = int(input('duration = '))

sec = duration % 60
min = duration // 60 % 60
hours = duration // 3600 % 24
days = duration // 86400

if duration <= 59:
    print(f'{sec} сек')
elif 59 < duration < 3600:
    print(f'{min} мин {sec} сек')
elif 3600 <= duration < 86400:
    print(f'{hours} час {min} мин {sec} сек')
else:
    print(f'{days} дн {hours} час {min} мин {sec} сек')