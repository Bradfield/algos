import unittest

from prims_spanning_tree import create_spanning_tree, example_graph

expected_tree = {
    'A': set(['B']),
    'B': set(['C', 'D']),
    'D': set(['E']),
    'E': set(['F']),
    'F': set(['G'])
}


class TestCorrectness(unittest.TestCase):

    def test_example_graph(self):
        self.assertEqual(
            create_spanning_tree(example_graph, 'A'),
            expected_tree
        )
