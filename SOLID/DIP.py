# Dependency Inversion Principle ( NOT related to dependency injection)
# High level classes/modules should not depend on low level modules, instead they should depend on abstraction(abstract)
# this is because if we change the low level class, it will break code on the high level module :(
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


# LOW LEVEL CLASS
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                yield r[2].name


# HIGH LEVEL CLASS
class Research:
    def __init__(self, browser):  # browser is an implementation of RelationshipBrowser class
        for p in browser.find_all_children_of("John"):
            print(p)


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)