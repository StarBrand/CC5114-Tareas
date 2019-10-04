"""test_move.py: Unit test for Move class"""

import numpy as np
from unittest import TestCase, main
from utils.simulations import DOWN


class MoveTest(TestCase):

    """Test DOWN, as an example"""

    def test_step(self):
        self.assertEqual(DOWN.step()[0], 1, "Not one as expected")

    def test_str_repr(self):
        self.assertEqual("DOWN", str(DOWN), "Not string expected")

    def test_sum(self):
        location = np.array([3, 3])
        transition = DOWN + location
        self.assertEqual(5, transition[0], "Wrong first coordinate")
        self.assertEqual(3, transition[1], "Wrong second coordinate")


if __name__ == '__main__':
    main()
