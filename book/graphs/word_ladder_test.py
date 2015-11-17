import unittest

from word_ladder import traverse, word_graph


class TestCorrectness(unittest.TestCase):

    def assert_path_to_find_word(self, from_word, to_word, expected_path):
        for word, path in traverse(word_graph, from_word):
            if expected_path:
                if word == to_word:
                    self.assertEqual(path, expected_path)
            else:
                self.assertNotEqual(word, to_word)

    def test_traverses_correctly(self):
        self.assert_path_to_find_word('FOOL', 'SAGE', [
            'FOOL', 'FOOD', 'FOLD', 'SOLD', 'SOLE', 'SALE', 'SAGE'])
        self.assert_path_to_find_word('TREE', 'PEAR', [
            'TREE', 'PREE', 'PREP', 'PEEP', 'PEER', 'PEAR'])
        self.assert_path_to_find_word('TREE', 'AAAA', None)


if __name__ == '__main__':
    unittest.main()
