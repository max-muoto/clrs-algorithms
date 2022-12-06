import heapq


class Node:
    def __init__(self, val, freq, left=None, right=None):
        self.val = val
        self.freq = freq
        self.left = left
        self.right = right


def huffman(c):
    n = len(c)
    heapq.heapify(c)
    for _ in range(0, n-1):
        x = heapq.heappop(c)
        y = heapq.heappop(c)
        freq = x[0] + y[0]
        left = x[1]
        right = y[1]
        z = Node(None, freq, left, right)
        heapq.heappush(c, (freq, z))
    return heapq.heappop(c)


def main():
    chars = [(5, Node("A", 5)), (9, Node("E", 9)), (12, Node("C", 12)),
             (13, Node("B", 13)), (16, Node("D", 16)), (45, Node("A", 45))]
    # Root node for the tree
    node = huffman(chars)[1]
    print(node.freq)


if __name__ == "__main__":
    main()
