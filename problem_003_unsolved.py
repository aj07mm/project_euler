import unittest
import sys
import functools
from itertools import combinations
from operator import mul

def is_prime(n):
    number_of_divisions = 0
    for m in range(1, n+1):
        if n % m == 0:
            number_of_divisions += 1

    return number_of_divisions == 2


def get_primes(n):
    primes = []
    for m in range(0, n+1, 2):
        if is_prime(m):
            primes.append(m)

    yield primes
        

def largest_prime_factor(n):
    primes = []
    res = []

    print("get all possible combinations")
    # get all possible combinations with length being 2 until len(str(n))+1
    for m in range(2, len(str(n))+1):
        for combination in combinations(get_primes(n), m):
            print(combination)
            # if the product of all numbers is n, give me the max of that combination
            if functools.reduce(mul, combination, 1) == n:
                return max(combination)

    return None
    

class TestIsPrime(unittest.TestCase):

    def test_1_1(self):
        self.assertFalse(is_prime(1))

    def test_1_2(self):
        self.assertTrue(is_prime(2))

    def test_1_3(self):
        self.assertTrue(is_prime(3))

    def test_1_96(self):
        self.assertFalse(is_prime(96))

    def test_1_97(self):
        self.assertTrue(is_prime(97))


class TestLargestPrimeFactor(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(largest_prime_factor(13195), 29)


if __name__ == '__main__':
    #unittest.main()
    print(largest_prime_factor(600851475143))
