position_name = ['инженер-конструктор Игорь',
                 'главный бухгалтер МАРИНА',
                 'токарь высшего разряда нИКОЛАй',
                 'директор аэлита'
                 ]

i = 0
while i < len(position_name):
    name = position_name[i].split()
    print('Привет,', name[-1].capitalize(), end='')
    print('!')
    i += 1
