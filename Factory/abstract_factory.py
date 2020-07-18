# abstract base class as a factory
from abc import ABC
from enum import auto, Enum


# our base class
class HotDrink(ABC):
    def consume(self):
        pass


# subclasses without constructor
class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious")


class Coffee(HotDrink):
    def consume(self):
        print("this coffee is too hot")


# constructors
class TeaFactory:
    def prepare(self, amount):
        print(f'put {amount} of water in the cup')
        return Tea()


class CoffeeFactory:
    def prepare(self, amount):
        print(f'put {amount} of coffee in the cup')
        return Coffee()


# class that works as an API for all other classes that we have defined
class HotDrinkMachine:
    class AvailableDrinks(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            # we loop through all enum options and create CoffeeFactory, TeaFactory,...
            for d in self.AvailableDrinks:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        for f in self.factories:
            print(f[0])  # get factory_name string from the tuple

        idx = 1
        return self.factories[idx][1].prepare(100)


drink = HotDrinkMachine().make_drink()
print(drink)
