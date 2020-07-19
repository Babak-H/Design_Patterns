# singleton is a class that is instantiated only once in a class

import random


class Database:
    initialized = False

    # in python, __init__ method gets called after __new__ by default
    def __init__(self):
        self.id = random.randint(1, 101)
        print(f'my id is {self.id}')

    _instance = None

    # create a new class instance if it doesnt exist, then return it
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1.id, d2.id)
    print(d1 == d2)
    print(database == d1)