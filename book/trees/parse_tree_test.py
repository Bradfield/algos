import unittest

from parse_tree import evaluate, build_parse_tree
from parse_tree_reverse import construct_expression

cases = (
    ('((7+3)*(5-2))', 30),
    ('(3+(4*5))', 23),
    ('((4*5)/2)', 10),
)


class TestCorrectness(unittest.TestCase):

    def test_parse_and_evaluate(self):
        for expression, expected_value in cases:
            self.assertEqual(
                evaluate(build_parse_tree(expression)),
                expected_value
            )

    def test_round_trip(self):
        for expression, _ in cases:
            self.assertEqual(
                construct_expression(build_parse_tree(expression)),
                expression
            )
