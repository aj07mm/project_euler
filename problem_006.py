# https://projecteuler.net/problem=6
import math
import unittest


def sum_square_difference(nth):
    sum_fo_squares = reduce(
        lambda acc, x: acc + math.pow(x, 2), 
        range(1, nth+1)
    )
    square_of_sum = math.pow(reduce(
        lambda acc, x: acc + x, 
        range(1, nth+1)
    ), 2)
    return square_of_sum - sum_fo_squares
        



class TestSmallestMultiple(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(sum_square_difference(10), 2640)

    def test_1_2(self):
        self.assertEqual(sum_square_difference(100), 25164150)


if __name__ == '__main__':
    unittest.main()
