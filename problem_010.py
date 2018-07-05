# https://projecteuler.net/problem=10
import math
import unittest
from multiprocessing import Pool, Process


def sieve_of_eratosthenes(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            print (i)
            for j in range(i*i, n+1, i):
                multiples.append(j)


def sieve_of_atkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
        print(x, y)
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P


def summation_of_primes(nth):
    return sum(sieve_of_atkin(nth))


class TestSummationOfPrimes(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(summation_of_primes(2000000), 142913828922)


if __name__ == '__main__':
    unittest.main()
