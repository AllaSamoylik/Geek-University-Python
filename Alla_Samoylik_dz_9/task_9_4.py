class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал(а)')

    def stop(self):
        print(f'{self.name} остановился(ась)')

    def turn(self, direction):
        print(f'{self.name} повернул(а) {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость: {self.speed} км/ч')
        else:
            print('Превышена скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость: {self.speed} км/ч')
        else:
            print('Превышена скорость!')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


renault = TownCar(50, 'красная', 'Renault Sandero')
skoda = TownCar(100, 'чёрная', 'Skoda Rapid')
bugatti = SportCar(200, 'жёлтая', 'Bugatti')
tractor = WorkCar(45, 'серый', 'Трактор')
pps = PoliceCar(80, 'синий', 'ППС')

renault.go()
renault.show_speed()
renault.turn('налево')
renault.stop()
print('-' * 15)
skoda.go()
skoda.show_speed()
print('-' * 15)
bugatti.go()
bugatti.show_speed()
print('-' * 15)
tractor.go()
tractor.turn('направо')
print('-' * 15)
pps.go()
print(pps.is_police)
