import heapq
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
    vertices: Dict[str, Node] = {}

    def add_edge(self, node1, node2, weight):
        if node1 in self.vertices:
            self.vertices[node1].add_weight(node2, weight)
        else:
            first_node = Node(node1)
            first_node.add_weight(node2, weight)
            self.vertices[node1] = first_node

        if node2 in self.vertices:
            self.vertices[node2].add_weight(node1, weight)
        else:
            second_node = Node(node2)
            second_node.add_weight(node1, weight)
            self.vertices[node2] = second_node

    def prims(self, root):
        parents = {}
        min_dist = {}
        pq = []
        min_dist[root] = 0
        for vertex in self.vertices:
            if vertex != root:
                min_dist[vertex] = float("inf")
            parents[vertex] = None
            heapq.heappush(pq, (min_dist[vertex], vertex))
        while pq:
            curr = heapq.heappop(pq)
            curr_vertex = curr[1]
            for vertex in self.vertices[curr_vertex].weights:
                if (min_dist[vertex], vertex) in pq and self.vertices[curr_vertex].weights[vertex] < min_dist[vertex]:
                    parents[vertex] = curr_vertex
                    min_dist[vertex] = self.vertices[curr_vertex].weights[vertex]
                    heapq.heappush(pq, (min_dist[vertex], vertex))

        print(parents)
        print(min_dist)

        return None


def main():
    graph = Graph()
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 3)
    graph.add_edge("A", "D", 3)
    graph.add_edge("C", "D", 5)
    graph.add_edge("B", "C", 4)
    graph.add_edge("E", "B", 3)
    graph.add_edge("C", "E", 1)
    graph.add_edge("D", "E", 7)
    graph.add_edge("F", "E", 8)
    graph.add_edge("F", "G", 9)
    graph.add_edge("F", "C", 6)
    graph.prims("A")


if __name__ == "__main__":
    main()
