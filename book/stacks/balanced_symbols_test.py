import unittest

from balanced_symbols import is_balanced


class TestCorrectness(unittest.TestCase):

    def test_identifies_valid_sequence(self):
        self.assertTrue(is_balanced('()'))
        self.assertTrue(is_balanced('()(())'))
        self.assertTrue(is_balanced('{{([][])}()}'))

    def test_identifies_left_imbalance(self):
        self.assertFalse(is_balanced('(()'))

    def test_identifies_right_imbalance(self):
        self.assertFalse(is_balanced('())'))

    def test_identifies_mismatch(self):
        self.assertFalse(is_balanced('{[])'))


if __name__ == '__main__':
    unittest.main()
