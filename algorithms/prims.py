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


def main():
    graph = Graph(GraphType.DIRECTED)
    graph.add_vertices(["A", "B", "C", "D", "E", "F", "G"])
    graph.add_edges([("A", "B", 2), ("A", "C", 3),
                    ("A", "D", 3), ("C", "D", 5), ("B", "C", 4), ("B", "C", 4), ("E", "B", 3), ("C", "E", 1), ("D", "E", 7), ("F", "E", 8), ("F", "G", 9), ("F", "C", 6)])
    print(Prims.minimum_spanning_tree(graph, "A"))


if __name__ == "__main__":
    main()
