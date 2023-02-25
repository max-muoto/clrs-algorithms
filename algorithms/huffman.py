import heapq
from typing import Optional

from utility_classes.tree_node import TreeNode


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
    def compress(nodes) -> HuffmanNode:
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
