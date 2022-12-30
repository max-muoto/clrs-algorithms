import heapq
from utility_classes.graph import Graph, GraphType


class Prims:
    @staticmethod
    def minimum_spanning_tree(graph: Graph, root: str):
        vertex_adjs = graph.vertex_adjacencies

        parents = {}
        min_dist = {}
        pq = []
        min_dist[root] = 0
        for vertex in vertex_adjs:
            if vertex != root:
                min_dist[vertex] = float("inf")
            parents[vertex] = None
            heapq.heappush(pq, (min_dist[vertex], vertex))

        while pq:
            curr = heapq.heappop(pq)
            curr_vertex = curr[1]
            for vertex in vertex_adjs[curr_vertex]:
                if (min_dist[vertex], vertex) in pq and vertex_adjs[curr_vertex][
                    vertex
                ] < min_dist[vertex]:
                    parents[vertex] = curr_vertex
                    min_dist[vertex] = vertex_adjs[curr_vertex][vertex]
                    heapq.heappush(pq, (min_dist[vertex], vertex))

        return parents
