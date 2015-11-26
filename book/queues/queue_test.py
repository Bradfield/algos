import unittest

from queue import Queue

cases = (
    (lambda q: q.is_empty(), [], True),
    (lambda q: q.enqueue(4), [4], None),
    (lambda q: q.enqueue('dog'), ['dog', 4], None),
    (lambda q: q.enqueue(True), [True, 'dog', 4], None),
    (lambda q: q.size(), [True, 'dog', 4], 3),
    (lambda q: q.is_empty(), [True, 'dog', 4], False),
    (lambda q: q.enqueue(8.4), [8.4, True, 'dog', 4], None),
    (lambda q: q.dequeue(), [8.4, True, 'dog'], 4),
    (lambda q: q.dequeue(), [8.4, True], 'dog'),
    (lambda q: q.size(), [8.4, True], 2),
)


class TestCorrectness(unittest.TestCase):

    def test_operates_correctly(self):
        queue = Queue()
        for operate, expected_state, expected_return in cases:
            actual_return = operate(queue)
            self.assertEqual(actual_return, expected_return)
            self.assertEqual(queue._items, expected_state)


if __name__ == '__main__':
    unittest.main()
