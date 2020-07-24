"""
Consider the code presented below. We have two classes called SingleValue and ManyValues. SingleValue stores just
one numeric value, but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values
that the object contains. Please ensure that there is only a single method that realizes the property sum,
not multiple methods.
"""
from unittest import TestCase
from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            for i in c:  # if it is a number or just a SingleValue, c and i are same
                result += i
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    # when it is being looped through, return the object's value
    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass


class Evaluate(TestCase):
    def test_exercise(self):
        single_value = SingleValue(11)

        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)

        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)

        self.assertEqual(all_values.sum, 66)
