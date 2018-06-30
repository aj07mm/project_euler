import unittest

def common_multiples_sum(a, b, below):
    multiples = []
    for n in range(1, below+1):
        result = a * n
        if result < below:
            multiples.append(result)

        result = b * n
        if result < below:
            multiples.append(result)

    return sum(set(multiples))

class TestCommonMultiples(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(common_multiples_sum(1, 1, 10), 1)

    def test_3_5(self):
        self.assertEqual(common_multiples_sum(3, 5, 10), 23)

    def test_3_5(self):
        self.assertEqual(common_multiples_sum(3, 5, 1000), 233168)

if __name__ == '__main__':
    unittest.main()


