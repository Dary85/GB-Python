from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def __init__(self, v=0.0):
        self.v = v

    @property
    def calc(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h=0.0):
        self.h = h

    @property
    def calc(self):
        return self.h / 2 + 0.3


c1 = Coat(46)
c2 = Costume(165)
print(f"Total {c1.calc + c2.calc:2f}")
