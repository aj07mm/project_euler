import unittest
import sys

sys.setrecursionlimit(4000000)

# 1 1 2 3 5 8
def even_fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return even_fibonacci_recursion(n-1) + even_fibonacci_recursion(n-2)


def even_fibonacci_iter(n):
    if n < 2:
        return n
    fibPrev = 1
    fib = 1
    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib


class TestCommonMultiples(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(even_fibonacci_iter(4000000), 2)

if __name__ == '__main__':
    unittest.main()


