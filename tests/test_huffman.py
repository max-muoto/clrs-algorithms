import unittest
from algorithms.huffman import Huffman, HuffmanNode


class HuffmanTest(unittest.TestCase):
    def test_simple_huffman_encoding(self):
        chars = [
            (5, HuffmanNode("A", 5)),
            (9, HuffmanNode("E", 9)),
            (12, HuffmanNode("C", 12)),
            (13, HuffmanNode("B", 13)),
            (16, HuffmanNode("D", 16)),
            (45, HuffmanNode("A", 45)),
        ]

        node = Huffman.compress(chars)[1]
        self.assertEqual(node.freq, 100)


if __name__ == "__main__":
    unittest.main()
