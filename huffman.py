import heapq

from tree_node import TreeNode


class HuffmanNode(TreeNode):
    def __init__(self, val, freq, left=None, right=None):
        super().__init__(val, left, right)
        self.freq = freq


def huffman(c):
    n = len(c)
    heapq.heapify(c)
    for _ in range(0, n-1):
        x = heapq.heappop(c)
        y = heapq.heappop(c)
        freq = x[0] + y[0]
        left = x[1]
        right = y[1]
        z = HuffmanNode(None, freq, left, right)
        heapq.heappush(c, (freq, z))
    return heapq.heappop(c)


def main():
    chars = [(5, HuffmanNode("A", 5)), (9, HuffmanNode("E", 9)), (12, HuffmanNode("C", 12)),
             (13, HuffmanNode("B", 13)), (16, HuffmanNode("D", 16)), (45, HuffmanNode("A", 45))]
    # Root node for the tree
    node = huffman(chars)[1]
    print(node.freq)


if __name__ == "__main__":
    main()
