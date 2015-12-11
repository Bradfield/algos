import unittest

from binary_heap import BinaryHeap

cases = (
    [3, 2, 1, 4, 2],
    [-1, -2, -4, -6],
    [3],
    [0, -1, 5],
    [1.1, 0, -5, 20, 1e7],
)


class TestCorrectness(unittest.TestCase):

    def test_correctness(self):
        for case in cases:
            bheap = BinaryHeap()
            bheap.build_heap(case)
            self.assertEqual(bheap.items[1:], sorted(case))
