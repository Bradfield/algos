import unittest

from lattice_traversal_recursive import num_paths as num_paths_recursive

cases = (
    (0, 0, 1),
    (1, 1, 2),
    (1, 2, 3),
    (2, 1, 3),
    (2, 2, 6),
    (3, 2, 10),
    (2, 3, 10),
    (3, 3, 20)
)


class TestCorrectness(unittest.TestCase):

    def test_correctness(self):
        for f in (num_paths_recursive,):
            for h, w, expected in cases:
                self.assertEqual(f(h, w), expected)
