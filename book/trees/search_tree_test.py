import unittest

from avl_tree import AVLTree
from binary_search_tree import BinarySearchTree


pairs = (
    (1, 3),
    (5, True),
    (2, 'a'),
    (3, 2),
    (10, 0.1)
)


class TestCorrectness(unittest.TestCase):

    def test_put_and_get(self):
        for TreeClass in (AVLTree, BinarySearchTree):
            tree = TreeClass()
            for key, value in pairs:
                tree[key] = value
            for key, value in pairs:
                self.assertEqual(tree[key], value)

    def test_delete(self):
        for TreeClass in (AVLTree, BinarySearchTree):
            tree = TreeClass()
            tree[1] = 2
            self.assertEqual(tree[1], 2)
            tree.delete(1)
            with self.assertRaises(KeyError):
                tree[1]

    def test_iteration(self):
        for TreeClass in (AVLTree, BinarySearchTree):
            tree = TreeClass()
            for key, value in pairs:
                tree[key] = value
            self.assertEqual(
                [item for item in tree],
                [k for k, v in sorted(pairs)]
            )
