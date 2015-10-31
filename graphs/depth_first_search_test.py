import imp
import os
import unittest

dirname = os.path.dirname(os.path.realpath(__file__))
source_file = os.path.join(dirname, 'depth-first-search.md')
depth_first_search = imp.load_source('depth_first_search', source_file)

traversal_times = depth_first_search.traversal_times

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
