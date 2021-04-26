from abc import ABC, abstractmethod


class Clothers(ABC):
    @abstractmethod
    def calculate_fabric_consumption(self):
        pass


class Coat(Clothers):
    def __init__(self, v):
        self.v = v

    @property
    def calculate_fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothers):
    def __init__(self, h):
        self.h = h

    @property
    def calculate_fabric_consumption(self):
        return self.h * 2 + 0.3


c = Coat(40)
print(c.calculate_fabric_consumption)
s = Suit(190)
print(s.calculate_fabric_consumption)
