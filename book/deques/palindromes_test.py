import unittest

from palindromes import is_palindrome

cases = (
    ('lsdkjfskf', False),
    ('radar', True),
    ('racecar', True),
)


class TestCorrectness(unittest.TestCase):
    def test_identifies_palindromes(self):
        for word, expectation in cases:
            self.assertEqual(is_palindrome(word), expectation)
