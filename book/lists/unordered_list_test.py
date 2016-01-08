import unittest

from unordered_list import UnorderedList


class CorrectnessTest(unittest.TestCase):
    def test_adding(self):
        l = UnorderedList()
        self.assertEqual(l.size(), 0)
        self.assertTrue(l.is_empty())
        l.add(1)
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.head.value, 1)
        self.assertFalse(l.is_empty())
        l.add(2)
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.head.value, 2)

    def test_searching(self):
        l = UnorderedList()
        for i in range(4):
            l.add(i)
        for i in range(4):
            self.assertTrue(l.search(i))
        for item in (5, None, True, "blah"):
            self.assertFalse(l.search(item))

    def test_remove(self):
        l = UnorderedList()
        for i in range(3):
            l.add(i)
        # remove from middle
        l.remove(1)
        self.assertFalse(l.search(1))
        self.assertEqual(l.size(), 2)
        # remove from end
        l.remove(2)
        self.assertFalse(l.search(2))
        self.assertEqual(l.size(), 1)
        # remove from start
        l.remove(0)
        self.assertFalse(l.search(0))
        self.assertEqual(l.size(), 0)
