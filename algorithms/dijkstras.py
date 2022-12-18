from queue import PriorityQueue

from utility_classes.graph import Graph

class Dijkstras:
    @staticmethod
    def shortest_path(graph: Graph, source: str):
        vertices = graph.vertices
        edges = graph.edges

        distances = {}
        previous_nodes = {}
        pq = PriorityQueue()

        # Init single-source and insert each vertex in the priority queue
        distances[source] = 0
        for vertex in vertices:
            if vertex != source:
                distances[vertex] = float("inf")
                previous_nodes[vertex] = "None"
            pq.put((distances[vertex], vertex))

        while not pq.empty():
            # Get vertex with min distance from PQ
            curr_set = pq.get()
            curr_vertex = curr_set[1]
            for adjacent_vertex in edges[curr_vertex]:
                # Check if we can decrease the distance
                possible_value = (
                    distances[curr_vertex] +
                    edges[curr_vertex][adjacent_vertex]
                )

                # If so, update our dictionaries and the PQ
                if possible_value < distances[adjacent_vertex]:
                    distances[adjacent_vertex] = possible_value
                    previous_nodes[adjacent_vertex] = curr_vertex
                    # Decrease key in PQ.
                    pq.put((possible_value, adjacent_vertex))
        return distances
