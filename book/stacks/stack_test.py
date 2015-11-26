import unittest

from stack_left import Stack as StackLeft
from stack_right import Stack as StackRight


cases = (
    (lambda s: s.is_empty(), [], True),
    (lambda s: s.push(4), [4], None),
    (lambda s: s.push('dog'), [4, 'dog'], None),
    (lambda s: s.peek(), [4, 'dog'], 'dog'),
    (lambda s: s.push(True), [4, 'dog', True], None),
    (lambda s: s.size(), [4, 'dog', True], 3),
    (lambda s: s.is_empty(), [4, 'dog', True], False),
    (lambda s: s.push(8.4), [4, 'dog', True, 8.4], None),
    (lambda s: s.pop(), [4, 'dog', True], 8.4),
    (lambda s: s.pop(), [4, 'dog'], True),
    (lambda s: s.size(), [4, 'dog'], 2),
)


class TestCorrectness(unittest.TestCase):

    def assert_operates_correctly(self, stack_class, state_relationship):
        stack = stack_class()
        for operate, expected_state, expected_return in cases:
            actual_return = operate(stack)
            self.assertEqual(actual_return, expected_return)
            self.assertEqual(stack._items, state_relationship(expected_state))

    def test_stack_left_correctness(self):
        self.assert_operates_correctly(StackLeft,
                                       lambda xs: list(reversed(xs)))

    def test_stack_right_correctness(self):
        self.assert_operates_correctly(StackRight, lambda xs: xs)


if __name__ == '__main__':
    unittest.main()
