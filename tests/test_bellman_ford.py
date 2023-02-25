import unittest

from algorithms.bellman_ford import BellmanFord
from utility_classes.graph import Graph, GraphType


class BellmanFordTest(unittest.TestCase):
    def test_simple_shortest_path_undirected(self):
        graph = Graph(GraphType.UNDIRECTED_WEIGHTED)
        graph.add_vertices(["A", "B", "C", "D", "E"])
        graph.add_edges(
            [
                ("A", "B", 6),
                ("A", "D", 1),
                ("B", "D", 2),
                ("D", "E", 1),
                ("B", "E", 2),
                ("B", "C", 5),
                ("E", "C", 5),
            ]
        )
        shortest_paths = {"A": 0, "B": 3, "D": 1, "E": 2, "C": 7}
        self.assertEqual(BellmanFord.shortest_path(graph, "A"), shortest_paths)
        shortest_paths = {"A": 3, "B": 0, "D": 2, "E": 2, "C": 5}
        self.assertEqual(BellmanFord.shortest_path(graph, "B"), shortest_paths)
        shortest_paths = {"A": 7, "B": 5, "D": 6, "E": 5, "C": 0}
        self.assertEqual(BellmanFord.shortest_path(graph, "C"), shortest_paths)

    def test_simple_shortest_path_directed(self):
        graph = Graph(GraphType.DIRECTED_WEIGHTED)
        graph.add_vertices(["A", "B", "C", "D", "E"])
        graph.add_edges(
            [
                ("A", "B", 6),
                ("A", "D", 1),
                ("B", "D", 2),
                ("D", "E", 1),
                ("B", "E", 2),
                ("B", "C", 5),
                ("E", "C", 5),
            ]
        )
        shortest_paths = {"A": 0, "B": 6, "D": 1, "E": 2, "C": 7}
        self.assertEqual(BellmanFord.shortest_path(graph, "A"), shortest_paths)
        shortest_paths = {"A": float("inf"), "B": 0, "D": 2, "E": 2, "C": 5}
        self.assertEqual(BellmanFord.shortest_path(graph, "B"), shortest_paths)
        shortest_paths = {
            "A": float("inf"),
            "B": float("inf"),
            "D": float("inf"),
            "E": float("inf"),
            "C": 0,
        }
        self.assertEqual(BellmanFord.shortest_path(graph, "C"), shortest_paths)


if __name__ == "__main__":
    unittest.main()
