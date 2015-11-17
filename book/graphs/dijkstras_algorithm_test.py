import unittest

from dijkstras_algorithm import example_graph, calculate_distances


CORRECT_DISTANCES = {
    'X': {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2},
    'Y': {'U': 2, 'V': 3, 'W': 1, 'X': 1, 'Y': 0, 'Z': 1},
    'Z': {'U': 3, 'V': 4, 'W': 2, 'X': 2, 'Y': 1, 'Z': 0}
}


class TestCorrectness(unittest.TestCase):

    def test_calculates_correctl(self):
        for starting_vertex, distances in CORRECT_DISTANCES.items():
            self.assertEqual(
                calculate_distances(example_graph, starting_vertex),
                distances)


if __name__ == '__main__':
    unittest.main()
