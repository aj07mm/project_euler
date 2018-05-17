import unittest
import sys
from itertools import combinations


def is_prime(n):
    number_of_divisions = 0
    for m in range(1, n+1):
        if n % m == 0:
            number_of_divisions += 1
    
    return number_of_divisions == 2
        

def largest_prime_factor(n):
    primes = []
    for m in range(1, n+1):
        if is_prime(m):
            primes.append(m)

    #res = []
    #for n1 in combinations(primes, 4):
    #    if n1*n2*n3*n4 == n:
    #        res.append(n1, n2, n3, n4)
    return primes
    

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
    unittest.main()
