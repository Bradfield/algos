import unittest

from binary_conversion import convert_to_binary


class TestCorrectness(unittest.TestCase):

    def test_converts_to_binary(self):
        for i in range(1, 1000):
            self.assertEqual(convert_to_binary(i), '{0:b}'.format(i))

if __name__ == '__main__':
    unittest.main()
