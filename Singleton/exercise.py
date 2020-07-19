"""
write a function called is_singleton(). this method takes a factory method that returns an object and its up to you to determine wether or not that 
object is singleton instance
"""
from unittest import TestCase
from copy import deepcopy

def is_singleton(factory):
    x = factory()
    y = factory()

    return x is y


class Evaluate(TestCase):
    def test_exercise(self):
        obj = [1, 2, 3]
        self.assertTrue(is_singleton(lambda: obj))
        
        # this will assert false because each instance of deepcopy will create a seperate object
        self.assertFalse(is_singleton(lambda: deepcopy(obj)))




