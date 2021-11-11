class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_of_pavement(self, mass_of_asphalt, thickness_of_pavement):
        result = self._length * self._width * mass_of_asphalt * thickness_of_pavement
        print(f'Для покрытия дороги шириной {self._width}м и длиной {self._length}м понадобится {result}т асфальта')


roadway = Road(20, 5000)
roadway.calc_of_pavement(25, 5)
