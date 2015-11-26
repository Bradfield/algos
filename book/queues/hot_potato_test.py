import unittest

from hot_potato import hot_potato

cases = (
    (
        ('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'),
        7,
        'Susan'
    ),
)


class TestCorrectness(unittest.TestCase):

    def test_solves_problem(self):
        for players, passes, expectation in cases:
            self.assertEqual(hot_potato(players, passes), expectation)
