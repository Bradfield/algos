import imp
import os
import unittest

dirname = os.path.dirname(os.path.realpath(__file__))
source_file = os.path.join(dirname, 'word-ladder.md')
word_ladder = imp.load_source('word_ladder', source_file)

traverse = word_ladder.traverse
word_graph = word_ladder.word_graph


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
