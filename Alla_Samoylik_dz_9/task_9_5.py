class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} начала писать ')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title} начал чертить ')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title} начал рисовать')


stationery_items = Stationery('Канцелярия')
blue_pen = Pen('Ручка')
green_pencil = Pencil('Карандаш')
red_handle = Handle('Маркер')

stationery_items.draw()
blue_pen.draw()
green_pencil.draw()
red_handle.draw()
