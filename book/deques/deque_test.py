import unittest

from deque import Deque

cases = (
    (lambda d: d.is_empty(), [], True),
    (lambda d: d.add_rear(4), [4], None),
    (lambda d: d.add_rear('dog'), ['dog', 4], None),
    (lambda d: d.add_front('cat'), ['dog', 4, 'cat'], None),
    (lambda d: d.add_front(True), ['dog', 4, 'cat', True], None),
    (lambda d: d.size(), ['dog', 4, 'cat', True], 4),
    (lambda d: d.is_empty(), ['dog', 4, 'cat', True], False),
    (lambda d: d.add_rear(8.4), [8.4, 'dog', 4, 'cat', True], None),
    (lambda d: d.remove_rear(), ['dog', 4, 'cat', True], 8.4),
    (lambda d: d.remove_front(), ['dog', 4, 'cat'], True)
)


class TestCorrectness(unittest.TestCase):

    def test_operates_correctly(self):
        deque = Deque()
        for operate, expected_state, expected_return in cases:
            actual_return = operate(deque)
            self.assertEqual(actual_return, expected_return)
            self.assertEqual(deque._items, expected_state)


if __name__ == '__main__':
    unittest.main()
