# https://projecteuler.net/problem=9
import math
from itertools import combinations
import unittest


def special_pythagorean_triplet(n):
    for a, b, c in combinations(range(1, 1000-2), 3):
        print(a,b,c)
        if (
            (a + b + c == n) and 
            (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2))
        ):
            return a * b * c


class TestSmallestMultiple(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(special_pythagorean_triplet(1000), 31875000)


if __name__ == '__main__':
    unittest.main()
