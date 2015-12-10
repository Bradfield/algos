import unittest

from parse_tree import evaluate, build_parse_tree

cases = (
    ('((7+3)*(5-2))', 30),
    ('(3+(4*5))', 23),
    ('((4*5)/2)', 10),
)


class TestCorrectness(unittest.TestCase):

    def test_correctness(self):
        for expression, expected_value in cases:
            self.assertEqual(
                evaluate(build_parse_tree(expression)),
                expected_value
            )
