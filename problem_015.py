# https://projecteuler.net/problem=10
import math
import unittest


def lattice_paths(grid):
    return grid


class TestCase(unittest.TestCase):
    def test_1_1(self):
        grid = (2, 2)
        self.assertEquals(lattice_paths(grid), 6)


if __name__ == '__main__':
    unittest.main()
