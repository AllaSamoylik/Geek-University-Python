class Worker:
    def __init__(self, name, surname, position, income=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = income.get('wage') if income else None
        self._bonus = income.get('bonus') if income else None


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        if self._wage and self._bonus:
            print(f'Доход с учётом премии - {self._wage + self._bonus} рублей')
        elif self._wage and self._bonus is None:
            print(f'Доход - {self._wage} рублей')
        else:
            print('Данных о доходе нет')


paving_machine_driver = Position('Иван', 'Иванов', '> водитель асфальтоукладчика <', {'wage': 50000, 'bonus': 20000})
road_grader_driver = Position('Пётр', 'Петров', '> водитель автогрейдера <', {'wage': 60000})
road_builder = Position('Сидр', 'Сидоров', '> дорожный рабочий <')

paving_machine_driver.get_full_name()
print(paving_machine_driver.position)
paving_machine_driver.get_total_income()
print('-' * 15)
road_grader_driver.get_full_name()
print(road_grader_driver.position)
road_grader_driver.get_total_income()
print('-' * 15)
road_builder.get_full_name()
print(road_builder.position)
road_builder.get_total_income()
