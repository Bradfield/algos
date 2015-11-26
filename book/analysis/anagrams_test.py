import unittest

from anagrams import (
    anagram_checking_off,
    anagram_sort_and_compare,
    anagram_count_compare,
    anagram_with_counter
)

cases = (
    ('apple', 'pleap', True),
    ('apple', 'applf', False),
    ('abcde', 'edcba', True),
    ('abcde', 'abcd', False),
)


class TestCorrectness(unittest.TestCase):

    def assert_correctness(self, f):
        for word1, word2, expectation in cases:
            self.assertEqual(f(word1, word2), expectation)
            self.assertEqual(f(word2, word1), expectation)

    def test_checking_off(self):
        self.assert_correctness(anagram_checking_off)

    def test_sort_and_compare(self):
        self.assert_correctness(anagram_sort_and_compare)

    def test_count_compare(self):
        self.assert_correctness(anagram_count_compare)

    def test_with_counter(self):
        self.assert_correctness(anagram_with_counter)


if __name__ == '__main__':
    unittest.main()
