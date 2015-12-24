import unittest

from ordered_list import OrderedList


class CorrectnessTest(unittest.TestCase):
    def test_adding(self):
        l = OrderedList()
        self.assertEqual(l.size(), 0)
        self.assertTrue(l.is_empty())
        l.add(1)
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.head.value, 1)
        self.assertFalse(l.is_empty())
        l.add(2)
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.head.value, 1)

    def test_searching(self):
        l = OrderedList()
        for i in range(4):
            l.add(i)
        for i in range(4):
            self.assertTrue(l.search(i))
