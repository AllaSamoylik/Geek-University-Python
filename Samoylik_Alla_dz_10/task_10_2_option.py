from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, title):
        self.title = title

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, title, coat_size):
        super().__init__(title)
        self.coat_size = coat_size

    @property
    def tissue_consumption(self):
        return round(self.coat_size / 6.5 + 0.5, 1)


class Suit(Clothes):

    def __init__(self, title, suit_size):
        super().__init__(title)
        self.suit_size = suit_size

    @property
    def tissue_consumption(self):
        return round(2 * self.suit_size + 0.3, 1)


classic_coat = Coat('классическое пальто', 48)
business_suit = Suit('деловой костюм', 1.8)

print(classic_coat.tissue_consumption)
print(business_suit.tissue_consumption)
print(classic_coat + business_suit)
