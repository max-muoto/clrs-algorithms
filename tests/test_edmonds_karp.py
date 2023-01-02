import unittest
from algorithms.edmonds_karps import EdmondsKarps
from utility_classes.graph import Graph, GraphType


class EdmondsKarpTest(unittest.TestCase):
    def test_simple_maximum_flow(self):
        graph = Graph(GraphType.DIRECTED_WEIGHTED)
        graph.add_vertices(["A", "B", "C", "D", "E", "F"])
        graph.add_edges(
            [
                ("A", "B", 7),
                ("A", "C", 8),
                ("B", "D", 5),
                ("D", "E", 2),
                ("C", "E", 10),
                ("D", "F", 3),
                ("E", "F", 12),
            ]
        )

        print(EdmondsKarps.maximum_flow(graph=graph, source="A", sink="F"))


if __name__ == "__main__":
    unittest.main()
