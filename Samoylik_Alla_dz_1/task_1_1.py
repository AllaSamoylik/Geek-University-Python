duration = int(input('duration = '))

seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 3600 % 24
days = duration // 86400

if duration <= 59:
    print(f'{seconds} сек')
elif 59 < duration < 3600:
    print(f'{minutes} мин {seconds} сек')
elif 3600 <= duration < 86400:
    print(f'{hours} час {minutes} мин {seconds} сек')
else:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
