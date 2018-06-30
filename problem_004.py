# https://projecteuler.net/problem=4
import math
import unittest
from itertools import product


def is_palidrome(n):
    return str(n) == str(n)[::-1]
        

class TestIsPalindrome(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(is_palidrome(10), False)

    def test_1_2(self):
        self.assertEqual(is_palidrome(11), True)

    def test_1_3(self):
        self.assertEqual(is_palidrome(113), False)

    def test_1_4(self):
        self.assertEqual(is_palidrome(1), True)

    def test_1_5(self):
        self.assertEqual(is_palidrome(9009), True)

    def test_1_6(self):
        self.assertEqual(is_palidrome(111), True)

    def test_1_7(self):
        self.assertEqual(is_palidrome(1111), True)

    def test_1_8(self):
        self.assertEqual(is_palidrome(101), True)


def largest_palindrome_product():
    possible_numbers = [str(ch) for ch in range(1, 10)]
    palindromes = []
    for n1, n2, n3 in product(possible_numbers, repeat=3):
        number_1 = int(n1 + n2 + n3)
        for n21, n22, n23 in product(possible_numbers, repeat=3):
            number_2 = int(n21 + n22 + n23)
            product_palindrome = number_1 * number_2
            if is_palidrome(product_palindrome):
                palindromes.append(product_palindrome)

    return max(palindromes)
            
    


class TestLargestPalindromeProduct(unittest.TestCase):
    '''
        _ _ _ * _ _ _
    '''

    def test_1_1(self):
        self.assertEqual(largest_palindrome_product(), 906609)


if __name__ == '__main__':
    unittest.main()
