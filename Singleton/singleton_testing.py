import unittest

# here we can see the problem with singleton pattern. the way Database class is defined, there is no way to inject a new dataSource 
# to it for testing purposes


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


# this class's init will be executed only once
class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open('capitals.txt', 'r')
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            self.population[lines[i].strip()] = int(lines[i+1].strip())
        f.close()


# problem is that here we are forcing user to connect to a live (changable) database, which is very bad when testing and might lead to test failure
class SingletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for c in cities:
            result += Database().population[c]

        return result


# better approach would be allowing injection of a dummy (mock) database, for testing purposes
class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        result = 0
        for c in cities:
            result += self.db.population[c]
        return result


class DummyDB:
    population = {
        'alpha': 1,
        'beta': 2,
        'gamma': 3
    }

    def get_population(self, name):
        return self.population[name]


class SingletonTests(unittest.TestCase):
    def test_is_singleton(self):
        db = Database()
        db2 = Database()
        self.assertEqual(db, db2)

    def test_singleton_total_pops(self):
        """this test is on a live database :( """
        rf = SingletonRecordFinder()
        names = ['Seoul', 'Mexico City']
        tp = rf.total_population(names)
        # this will fail if we change the database
        self.assertEqual(tp, 1000+1000)

    mockDB = DummyDB()

    def test_dependant_total_pops(self):
       crf = ConfigurableRecordFinder(self.mockDB) 
       self.assertEqual(crf.total_population(['alpha', 'beta']), 3)


if __name__ == '__main__':
    unittest.main()
