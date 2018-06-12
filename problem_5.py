# https://projecteuler.net/problem=4
import math
import unittest
from itertools import product


def smallest_multiple(n):
    current_number = 1
    current_number_division_count = 0
    while True:

        for m in range(1, n+1):
            if current_number % m == 0:
                current_number_division_count += 1
        if current_number_division_count == n:
            return current_number

        print(current_number)
        print(current_number_division_count)

        # reset for new iteration
        current_number += 1
        current_number_division_count = 0



class TestSmallestMultiple(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(smallest_multiple(10), 2520)

    def test_1_2(self):
        self.assertEqual(smallest_multiple(20), 232792560)


if __name__ == '__main__':
    unittest.main()
