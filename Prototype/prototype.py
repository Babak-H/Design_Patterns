# Prototype is a partially or fully initialized object that you copy (clone) and make use of.

import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address  # object of class Address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('john', Address('123 London Road', 'London', 'UK'))

jane = copy.deepcopy(john)
jane.name = 'Jane'

print(john, '\n', jane)
