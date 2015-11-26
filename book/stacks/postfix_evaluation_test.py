import unittest

from postfix_evaluation import evaluate_postfix

cases = (
    ('7 8 + 3 2 + /', 3),
)


class TestCorrectness(unittest.TestCase):

    def test_converts_correctly(self):
        for postfix, expectation in cases:
            self.assertEqual(evaluate_postfix(postfix), expectation)


if __name__ == '__main__':
    unittest.main()
