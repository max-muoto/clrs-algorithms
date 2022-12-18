import heapq
from utility_classes.graph import Graph, GraphType


class Prims:
    @staticmethod
    def minimum_spanning_tree(graph: Graph, root: str):
        vertices = graph.vertices
        edges = graph.edges

        parents = {}
        min_dist = {}
        pq = []
        min_dist[root] = 0
        for vertex in vertices:
            if vertex != root:
                min_dist[vertex] = float("inf")
            parents[vertex] = None
            heapq.heappush(pq, (min_dist[vertex], vertex))

        while pq:
            curr = heapq.heappop(pq)
            curr_vertex = curr[1]
            for vertex in edges[curr_vertex]:
                if (min_dist[vertex], vertex) in pq and edges[curr_vertex][vertex] < min_dist[vertex]:
                    parents[vertex] = curr_vertex
                    min_dist[vertex] = edges[curr_vertex][vertex]
                    heapq.heappush(pq, (min_dist[vertex], vertex))

        return parents
