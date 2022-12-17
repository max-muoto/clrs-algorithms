import unittest
from dijkstras import Dijkstras

from graph import Graph, GraphType


class DijkstrasTest(unittest.TestCase):
    def test_simple_shortest_path(self):
        graph = Graph(GraphType.DIRECTED)
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
        self.assertEqual(Dijkstras(graph, "A"), shortest_paths)


if __name__ == "__main__":
    unittest.main()
