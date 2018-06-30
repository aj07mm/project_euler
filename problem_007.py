# https://projecteuler.net/problem=7
import math
import unittest


def is_prime(nth):
    acc = 0
    for n in range(1, nth+1):
        acc += 1 if nth % n == 0 else 0
        if acc > 2:
            return False
    return True


def get_prime(nth):
    primes = []
    n = 2 # starting with 2 because 1 isn't prime
    while len(primes) != nth:
        if is_prime(n):
            primes.append(n) 
        n += 1
    return primes[-1]


class TestSmallestMultiple(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(get_prime(10001), 104743)


if __name__ == '__main__':
    unittest.main()
