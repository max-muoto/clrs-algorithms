import heapq

from utility_classes.tree_node import TreeNode
from typing import Optional


class HuffmanNode(TreeNode):
    def __init__(
        self,
        val: str,
        freq: int,
        left: Optional["HuffmanNode"] = None,
        right: Optional["HuffmanNode"] = None,
    ):
        super().__init__(val, left, right)
        self.freq = freq


class Huffman:
    @staticmethod
    def compress(nodes):
        n = len(nodes)
        heapq.heapify(nodes)
        for _ in range(0, n - 1):
            x = heapq.heappop(nodes)
            y = heapq.heappop(nodes)
            freq = x[0] + y[0]
            left = x[1]
            right = y[1]
            z = HuffmanNode(None, freq, left, right)
            heapq.heappush(nodes, (freq, z))
        return heapq.heappop(nodes)


def main():
    chars = [
        (5, HuffmanNode("A", 5)),
        (9, HuffmanNode("E", 9)),
        (12, HuffmanNode("C", 12)),
        (13, HuffmanNode("B", 13)),
        (16, HuffmanNode("D", 16)),
        (45, HuffmanNode("A", 45)),
    ]
    # Root node for the tree
    node = Huffman.compress(chars)[1]
    print(node.freq)


if __name__ == "__main__":
    main()
