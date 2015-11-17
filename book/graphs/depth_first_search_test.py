import unittest

from depth_first_search import traversal_times

expected_traversal_times = {
    'A': {
        'finish': 12,
        'discovery': 1
    },
    'C': {
        'finish': 4,
        'discovery': 3
    },
    'B': {
        'finish': 11,
        'discovery': 2
    },
    'E': {
        'finish': 9,
        'discovery': 6
    },
    'D': {
        'finish': 10,
        'discovery': 5
    },
    'F': {
        'finish': 8,
        'discovery': 7
    }
}


class TestCorrectness(unittest.TestCase):

    def test_traverses_correctly(self):
        self.assertEqual(traversal_times, expected_traversal_times)

if __name__ == '__main__':
    unittest.main()
