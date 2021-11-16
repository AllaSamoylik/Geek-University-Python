from abc import ABC, abstractmethod


class Clothes(ABC):
    sum = 0

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes, ABC):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    @property
    def tissue_consumption(self):
        calc = round(self.size / 6.5 + 0.5, 1)
        Clothes.sum += calc
        return f'Для пошива изделия <{self.title}> потребуется {calc} м ткани'


class Suit(Clothes, ABC):

    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    @property
    def tissue_consumption(self):
        calc = round(2 * self.size + 0.3, 1)
        Clothes.sum += calc
        return f'Для пошива изделия <{self.title}> потребуется {calc} м ткани'


classic_coat = Coat('классическое пальто', 48)
business_suit = Suit('деловой костюм', 1.8)

print(classic_coat.tissue_consumption)
print(business_suit.tissue_consumption)
print(f'Общий расход ткани: {Clothes.sum} м')
