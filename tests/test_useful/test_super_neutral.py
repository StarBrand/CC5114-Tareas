"""test_super_neutral.py: The SuperNeutral float unittest"""

from random import uniform, seed
from unittest import TestCase, main
from useful.math_functions import SuperNeutral


class SuperNeutralTest(TestCase):

    def setUp(self) -> None:
        """
        Sets up unit testing
        """
        seed(2)
        self.testers = {
            "greater": float("Inf"),
            "lesser": -float("Inf"),
            "at_random1": uniform(-100, 0),
            "at_random2": uniform(-1, 1),
            "at_random3": uniform(0, 100),
            "additive_neutral": 0,
            "multiplicative_neutral": 1
        }

    def test_add(self):
        for key in self.testers:
            to_test = self.testers[key]
            self.assertEqual(to_test, to_test + SuperNeutral(), "Wrong add test with {}".format(key))
            self.assertEqual(to_test, SuperNeutral() + to_test, "Wrong add test with {}".format(key))

    def test_sub(self):
        for key in self.testers:
            to_test = self.testers[key]
            self.assertEqual(to_test, to_test - SuperNeutral(), "Wrong sub test with {}".format(key))
            self.assertEqual(to_test, SuperNeutral() - to_test, "Wrong sub test with {}".format(key))

    def test_max(self):
        for key in self.testers:
            to_test = self.testers[key]
            self.assertEqual(to_test, max(to_test, SuperNeutral()), "Wrong max test with {}".format(key))
            self.assertEqual(to_test, max(SuperNeutral(), to_test), "Wrong max test with {}".format(key))

    def test_mult(self):
        for key in self.testers:
            to_test = self.testers[key]
            self.assertEqual(to_test, to_test * SuperNeutral(), "Wrong mult test with {}".format(key))
            self.assertEqual(to_test, SuperNeutral() * to_test, "Wrong mult test with {}".format(key))

    def test_equal(self):
        a = SuperNeutral()
        b = SuperNeutral()
        self.assertEqual(a, SuperNeutral(), "Wrong equal with first variable")
        self.assertEqual(SuperNeutral(), a, "Wrong equal with first variable")
        self.assertEqual(b, SuperNeutral(), "Wrong equal with second variable")
        self.assertEqual(SuperNeutral(), b, "Wrong equal with second variable")
        self.assertEqual(SuperNeutral(), SuperNeutral(), "Wrong equal with two new ones")
        self.assertEqual(a, b, "Wrong equal with both variables")
        self.assertEqual(b, a, "Wrong equal with both variables")


if __name__ == '__main__':
    main()
