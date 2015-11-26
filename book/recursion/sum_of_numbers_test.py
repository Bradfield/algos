import unittest

from sum_of_numbers import iterative_sum, sum_of

cases = (
    ([1, 3, 5, 7, 9], 25),
    ([0], 0),
    ([], 0),
    ([-1, -2, -3], -6),
)


class TestCorrectness(unittest.TestCase):

    def test_correctness(self):
        for f in (iterative_sum, sum_of):
            for numbers, expected_sum in cases:
                self.assertEqual(f(numbers), expected_sum)
