import unittest

from base_conversion import to_string


class TestCorrectness(unittest.TestCase):

    def assert_matches_format_builtin(self, base, format_string):
        for i in range(1, 100):
            self.assertEqual(to_string(i, base), format_string.format(i))

    def test_converts_to_binary(self):
        self.assert_matches_format_builtin(2, '{0:b}')

    def test_converts_to_octal(self):
        self.assert_matches_format_builtin(8, '{0:o}')

    def test_converts_to_hex(self):
        self.assert_matches_format_builtin(16, '{0:x}')


if __name__ == '__main__':
    unittest.main()
