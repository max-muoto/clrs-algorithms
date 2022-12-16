from collections import defaultdict
from enum import Enum
from typing import Dict, Optional, Set, List, Union, Tuple


class GraphType(Enum):
    UNDIRECTED = 1
    DIRECTED = 2


class Graph:
    vertices: Set[str]
    edges: Dict[str, Union[Dict[str, int], Set[str]]]
    graph_type: GraphType

    def __init__(self, graph_type: GraphType):
        self.graph_type = graph_type
        if self.is_directed_graph():
            self.edges = defaultdict(dict)
        elif self.is_undirected_graph():
            self.edges = {}
        self.vertices = set()

    def is_directed_graph(self):
        return self.graph_type == GraphType.DIRECTED

    def is_undirected_graph(self):
        return self.graph_type == GraphType.UNDIRECTED

    def add_edge(self, u: str, v: str, weight: Optional[int]):
        if weight and self.is_directed_graph():
            self.edges[u][v] = weight
            self.edges[v][u] = weight
        elif self.is_undirected_graph():
            self.edges[u].add(v)
            self.edges[v].add(u)
        else:
            raise ValueError(
                "You incorrectly set the weight corresponding to the graph's type.")

    def add_edges(self, edges: Union[List[Tuple[str, str]], List[Tuple[str, str, int]]]):
        weighted_edges = len(edges[0]) == 3
        for edges in edges:
            u = edges[0]
            v = edges[1]
            if weighted_edges and self.is_directed_graph():
                weight = edges[2]
                self.edges[u][v] = weight
                self.edges[v][u] = weight
            elif self.is_undirected_graph():
                self.edges[u].add(v)
                self.edges[v].add(u)
            else:
                raise ValueError(
                    "You incorrectly set the weight corresponding to the graph's type.")

    def add_vertex(self, vertex_name: str):
        self.vertices.add(vertex_name)

    def add_vertices(self, vertex_names: List[str]):
        for vertex in vertex_names:
            self.vertices.add(vertex)
