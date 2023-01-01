import unittest
from algorithms.prims import Prims
from utility_classes.graph import Graph, GraphType


class PrimsTest(unittest.TestCase):
    def test_simple_mst(self):
        graph = Graph(GraphType.UNDIRECTED_WEIGHTED)
        graph.add_vertices(["A", "B", "C", "D", "E", "F", "G"])
        graph.add_edges(
            [
                ("A", "B", 2),
                ("A", "C", 3),
                ("A", "D", 3),
                ("C", "D", 5),
                ("B", "C", 4),
                ("B", "C", 4),
                ("E", "B", 3),
                ("C", "E", 1),
                ("D", "E", 7),
                ("F", "E", 8),
                ("F", "G", 9),
                ("F", "C", 6),
            ]
        )
        vertex_parents = {
            "D": "A",
            "G": "F",
            "C": "A",
            "F": "C",
            "B": "A",
            "E": "C",
            "A": None,
        }
        self.assertEqual(Prims.minimum_spanning_tree(graph, "A"), vertex_parents)


if __name__ == "__main__":
    unittest.main()
