"""
in BuilderFacets we have problem of breaking open/close pattern, so here we can inherit from each of the previous
builder classes. this way there is no need to change parent builder class after addition of each child subclass
"""


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name}, {self.position}, {self.date_of_birth}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


pb = PersonBirthDateBuilder()
me = pb.\
    called("Bob")\
    .works_as_a("programmer")\
    .born(92)\
    .build()

print(me)
