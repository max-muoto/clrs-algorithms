from utility_classes.graph import Graph
from typing import Dict


class BellmanFord:
    @staticmethod
    def shortest_path(graph: Graph, source: str) -> Dict[str, int]:
        vertex_adjs = graph.vertex_adjacencies

        distances = {}
        previous_nodes = {}

        for vertex in vertex_adjs:
            distances[vertex] = float("inf")
            previous_nodes[vertex] = None

        distances[source] = 0

        for _ in range(len(vertex_adjs)):
            # Go through each edge.
            for u in vertex_adjs:
                for v in vertex_adjs[u]:
                    if distances[u] + vertex_adjs[u][v] < distances[v]:
                        distances[v] = distances[u] + vertex_adjs[u][v]
                        previous_nodes[v] = u

        for u in vertex_adjs:
            for v in vertex_adjs[u]:
                if distances[u] + vertex_adjs[u][v] < distances[v]:
                    raise ValueError("Negative edge weight cycle detected.")

        return distances
