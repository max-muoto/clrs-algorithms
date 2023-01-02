from utility_classes.graph import Graph


class EdmondsKarps:
    @staticmethod
    def maximum_flow(self, graph: Graph, source: str, sink: str) -> int:
        adj_vertices = graph.vertex_adjacencies
        edges = graph.edges

        maximum_flow = 0
        # Holds parent vertices to track paths.
        predecessors = {}
        # Initialize flow for each edge to 0.
        flows = {}
        for edge in edges:
            flows[edge] = 0

        while True:
            queue = []
            queue.append(source)

            # Run BFS from source.
            while queue:
                curr_vertex = queue.pop(0)
                for vertex in adj_vertices[curr_vertex]:
                    edge = (curr_vertex, vertex)
                    capacity = adj_vertices[curr_vertex][vertex]
                    if (
                        vertex in predecessors
                        and vertex != source
                        and capacity > flows[edge]
                    ):
                        predecessors[vertex] = edge
                        queue.append(vertex)

            # In this case, we found an augmenting path.
            # Add flow of the path to our maximum flow and to each edge in the path.
            # Subtract the flow of the path from the opposite edges.
            if sink in predecessors:
                curr_path_flow = float("inf")

                prev_vertex = sink
                curr_vertex = predecessors[prev_vertex]
                while curr_vertex in predecessors:
                    edge = (prev_vertex, curr_vertex)
                    curr_path_flow = (
                        min(curr_vertex, adj_vertices[curr_vertex][prev_vertex])
                        - flows[edge]
                    )

                prev_vertex = sink
                curr_vertex = predecessors[prev_vertex]
                while curr_vertex in predecessors:
                    edge = (prev_vertex, curr_vertex)
                    flows[edge] += curr_path_flow
                    opposite_edge = (curr_vertex, prev_vertex)
                    flows[opposite_edge] -= curr_path_flow

                maximum_flow += curr_path_flow
            else:
                # There is no augmenting path so we have our maximum flow.
                break

        return maximum_flow
