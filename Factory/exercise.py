"""
you are given a class called Person. the person has two attributes: id, name

please implement a PersonFactory that has a non-static create_person() method that takes a person's name and returns a
person initialized with this name and an id.

the id of the person should be set as a 0-based index of the object created. so, the first person the factory makes
should have id=0, and second id=1, ...
"""
from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0  # its a class variable, because it doesnt have self property

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)