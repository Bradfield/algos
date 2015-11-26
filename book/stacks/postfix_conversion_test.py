import unittest

from postfix_conversion import infix_to_postfix

cases = (
    ('A * B + C * D', 'A B * C D * +'),
    ('( A + B ) * C - ( D - E ) * ( F + G )', 'A B + C * D E - F G + * -'),
    ('( A + B ) * ( C + D )', 'A B + C D + *'),
    ('( A + B ) * C', 'A B + C *'),
    ('A + B * C', 'A B C * +'),
)


class TestCorrectness(unittest.TestCase):

    def test_converts_correctly(self):
        for infix, expected_postfix in cases:
            self.assertEqual(infix_to_postfix(infix), expected_postfix)


if __name__ == '__main__':
    unittest.main()
