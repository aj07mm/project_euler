# https://projecteuler.net/problem=10
import math
import unittest
from multiprocessing import Pool

def is_prime(m):
    acc = 0
    for n in range(1, m+1):
        acc += 1 if m%n == 0 else 0
        if acc > 2:
            return False
    return True
        
def get_primes(nth_start, nth_end):
    primes = []
    for n in range(nth_start, nth_end+1):
        if is_prime(n):
            primes.append(n)
            print(len(primes))
    return primes
        

def summation_of_primes(nth_start, nth_end):
    return sum(get_primes(nth_start, nth_end))


def pool_fn(fn):
    p = Pool(2)
    res1 = p.map(fn, 2, 1000000)
    res2 = p.map(fn, 1000000, 2000000)


class TestSmallestMultiple(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(pool_fn(summation_of_primes), 123)


if __name__ == '__main__':
    unittest.main()
