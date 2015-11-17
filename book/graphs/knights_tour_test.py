import unittest

from knights_tour import find_solution_for, warnsdorffs_heuristic


class TestCorrectness(unittest.TestCase):

    def assert_valid_tour(self, board_size, tour):
        # tour is correct length
        self.assertEqual(board_size * board_size, len(set(tour)))
        for v1, v2 in zip(tour[:-1], tour[1:]):
            deltas = set([abs(v1[0] - v2[0]), abs(v1[1] - v2[1])])
            # each step is a valid knights move
            self.assertSetEqual(deltas, set([1, 2]))

    def test_small_boards_have_no_solution(self):
        for board_size in range(1, 5):
            self.assertFalse(find_solution_for(board_size))

    def test_size_five_board_no_heurisitc(self):
        board_size = 5
        tour = find_solution_for(board_size)
        self.assert_valid_tour(board_size, tour)

    def test_size_eight_board_with_warnsdorff(self):
        board_size = 8
        tour = find_solution_for(board_size, warnsdorffs_heuristic)
        self.assert_valid_tour(board_size, tour)


if __name__ == '__main__':
    unittest.main()
