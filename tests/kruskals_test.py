import unittest
from algorithms.kruskals import Kruskals
from utility_classes.graph import Graph, GraphType


class KruskalsTest(unittest.TestCase):
    def test_simple_mst(self):
        graph = Graph(GraphType.UNDIRECTED_WEIGHTED)
        graph.add_vertices(["A", "B", "C", "D", "E", "F"])
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
        mst = {("A", "B"), ("F", "E"), ("C", "E"), ("C", "D"), ("A", "C")}

        self.assertEqual(Kruskals.minimum_spanning_tree(graph), mst)


if __name__ == "__main__":
    unittest.main()
