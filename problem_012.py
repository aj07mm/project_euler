# https://projecteuler.net/problem=10
import math
import unittest
from multiprocessing import Pool, Process


# 1 = 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6


def get_divisors(n):
    n_divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            n_divisors += 1
    return n_divisors




def get_over_divisor(limit):
    n = 0
    n_divisors = 0
    previous_ns = []
    while n_divisors < limit:
        n += 1
        previous_ns.append(n)
        current_n = sum(previous_ns)
        print(current_n)
        n_divisors = get_divisors(current_n)
        if n_divisors > limit:
            return current_n


class TestSummationOfPrimes(unittest.TestCase):
    def test_1_1(self):
        self.assertGreater(get_divisors(28), 5)

    def test_1_2(self):
        get_over_divisor(500)
        #self.assertGreater(get_divisors(28), 500)


if __name__ == '__main__':
    unittest.main()
