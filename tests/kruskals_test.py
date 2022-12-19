import unittest
from algorithms.kruskals import KruskalsGraph


class KruskalsTest(unittest.TestCase):
    def test_simple_mst(self):
        graph = KruskalsGraph()
        graph.add_edge("A", "B", 1)
        graph.add_edge("A", "C", 3)
        graph.add_edge("A", "D", 3)
        graph.add_edge("C", "D", 2)
        graph.add_edge("B", "C", 4)
        graph.add_edge("E", "B", 3)
        graph.add_edge("C", "E", 1)
        graph.add_edge("D", "E", 3)
        graph.add_edge("F", "E", 2)
        graph.add_edge("F", "C", 9)
        mst = {('F', 'E'), ('E', 'C'), ('B', 'E'), ('A', 'B'), ('D', 'C')}
        self.assertEqual(graph.kruskals("A"), mst)


if __name__ == "__main__":
    unittest.main()
