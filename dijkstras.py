from typing import Dict
from queue import PriorityQueue


class Node:
    weights: Dict[str, int] = {}

    def __init__(self, name):
        self.name = name
        self.weights = {}

    def add_weight(self, node, weight):
        self.weights[node] = weight

    def get_weight(self, node):
        return self.weights[node]

    def get_weights(self):
        return self.weights


class Graph:
    nodes: Dict[str, Node] = {}

    def add_edge(self, node1, node2, weight):
        if node1 in self.nodes:
            self.nodes[node1].add_weight(node2, weight)
        else:
            first_node = Node(node1)
            first_node.add_weight(node2, weight)
            self.nodes[node1] = first_node

        if node2 in self.nodes:
            self.nodes[node2].add_weight(node1, weight)
        else:
            second_node = Node(node2)
            second_node.add_weight(node1, weight)
            self.nodes[node2] = second_node

    # Solve shortest-path using Dijkstra's Algorithm.
    def solve_shortest_path(self, source):
        distances = {}
        previous_nodes = {}
        pq = PriorityQueue()

        # Init single-source and insert each vertex in the priority queue
        distances[source] = 0
        for key in self.nodes:
            if key != source:
                distances[key] = float("inf")
                previous_nodes[key] = "None"
            pq.put((distances[key], key))

        while not pq.empty():
            # Get vertex with min distance from PQ
            curr_set = pq.get()
            curr_node = curr_set[1]
            for key in self.nodes[curr_node].weights:
                print("Current distances are: ", distances)
                # Relax

                # Check if we can decrease the distance
                possible_value = distances[curr_node] + \
                    self.nodes[curr_node].weights[key]

                # If so, update our dictionaries and the PQ
                if possible_value < distances[key]:
                    distances[key] = possible_value
                    previous_nodes[key] = curr_node
                    # Decrease key
                    pq.put((possible_value, key))
        return distances


def main():
    # Example graph
    graph = Graph()
    graph.add_edge("A", "B", 6)
    graph.add_edge("A", "D", 1)
    graph.add_edge("B", "D", 2)
    graph.add_edge("D", "E", 1)
    graph.add_edge("B", "E", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("E", "C", 5)
    print("Shortest-paths are: ", graph.solve_shortest_path("A"))


if __name__ == "__main__":
    main()
