class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_int(cls, date):
        value = date.split('-')
        return f'Дата: {int(value[0]):02d}, месяц: {int(value[1]):02d}, год: {int(value[2])}'

    @staticmethod
    def number_validation(date):
        value = date.split('-')
        day = int(value[0])
        month = int(value[1])
        year = int(value[2])
        # Если прям руками, не используя datetime.strptime(), то:
        if 1900 <= year <= 2100:
            if 1 <= month <= 12:
                if month == 2:
                    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                        return f'{day:02d}-{month:02d}-{year}' if 1 <= day <= 29 else f'Несуществующая дата'
                    else:
                        return f'{day:02d}-{month:02d}-{year}' if 1 <= day <= 28 else f'Несуществующая дата'
                elif month in [1, 3, 5, 7, 8, 10, 12]:
                    return f'{day:02d}-{month:02d}-{year}' if 1 <= day <= 31 else f'Несуществующая дата'
                else:
                    return f'{day:02d}-{month:02d}-{year}' if 1 <= day <= 30 else f'Несуществующая дата'
            else:
                return f'Несуществующий месяц'
        else:
            return f'Несуществующий год'


print(Date.date_int('01-02-1999'))
print(Date.number_validation('29-02-2024'))
print(Date.number_validation('31-04-2021'))
print(Date.number_validation('14-13-2006'))
