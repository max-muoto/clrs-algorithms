from queue import PriorityQueue

from graph import Graph, GraphType


class Dijkstras(Graph):
    def shortest_path(self, source):
        distances = {}
        previous_nodes = {}
        pq = PriorityQueue()

        # Init single-source and insert each vertex in the priority queue
        distances[source] = 0
        for vertex in self.vertices:
            if vertex != source:
                distances[vertex] = float("inf")
                previous_nodes[vertex] = "None"
            pq.put((distances[vertex], vertex))

        while not pq.empty():
            # Get vertex with min distance from PQ
            curr_set = pq.get()
            curr_vertex = curr_set[1]
            for adjacent_vertex in self.edges[curr_vertex]:
                # Check if we can decrease the distance
                possible_value = distances[curr_vertex] + \
                    self.edges[curr_vertex][adjacent_vertex]

                # If so, update our dictionaries and the PQ
                if possible_value < distances[adjacent_vertex]:
                    distances[adjacent_vertex] = possible_value
                    previous_nodes[adjacent_vertex] = curr_vertex
                    # Decrease key in PQ.
                    pq.put((possible_value, adjacent_vertex))
        return distances


def main():
    graph = Dijkstras(GraphType.DIRECTED)
    graph.add_vertices(["A", "B", "C", "D", "E"])
    graph.add_edges([("A", "B", 6), ("A", "D", 1), ("B", "D", 2),
                    ("D", "E", 1), ("B", "E", 2), ("B", "C", 5), ("E", "C", 5)])
    print("Shortest-paths are: ", graph.shortest_path("A"))


if __name__ == "__main__":
    main()
