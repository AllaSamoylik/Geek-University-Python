import time


class TrafficLight:
    __color = ['красный', 'жёлтый', 'зелёный']

    def running(self, counter):
        count = 0
        while count < counter:
            print(self.__color[0], end='')
            time.sleep(7)
            print('\r', end='')
            print(self.__color[1], end='')
            time.sleep(2)
            print('\r', end='')
            print(self.__color[2], end='')
            time.sleep(2)
            print('\r', end='')
            count += 1
        print(' ', end='')


light = TrafficLight()
light.running(2)
