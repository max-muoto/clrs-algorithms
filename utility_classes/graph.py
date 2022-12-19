from collections import defaultdict
from enum import Enum
from typing import Dict, Optional, Set, List, Union, Tuple


class GraphType(Enum):
    UNDIRECTED_UNWEIGHTED = 1
    UNDIRECTED_WEIGHTED = 2
    DIRECTED_UNWEIGHTED = 3
    DIRECTED_WEIGHTED = 4


class Graph:
    vertices: Set[str]
    edges: Dict[str, Union[Dict[str, int], Set[str]]]
    graph_type: GraphType

    def __init__(self, graph_type: GraphType):
        self.graph_type = graph_type
        if self.is_weighted_graph():
            self.edges = defaultdict(dict)
        else:
            self.edges = defaultdict(set)
        self.vertices = set()

    def is_directed_graph(self):
        return self.graph_type == GraphType.DIRECTED_UNWEIGHTED or self.graph_type == GraphType.DIRECTED_WEIGHTED 

    def is_weighted_graph(self):
        return self.graph_type == GraphType.UNDIRECTED_WEIGHTED or self.graph_type == GraphType.DIRECTED_WEIGHTED 


    def add_edge(self, u: str, v: str, weight: Optional[int]):
        if weight and self.is_weighted_graph():
            self.edges[u][v] = weight
            if not self.is_directed_graph():
                self.edges[v][u] = weight
        elif not self.is_weighted_graph():
            self.edges[u].add(v)
            if not self.is_directed_graph():
                self.edges[v].add(u)
        else:
            raise ValueError(
                "You incorrectly set the weight corresponding to the graph's type.")

    def add_edges(self, edges: Union[List[Tuple[str, str]], List[Tuple[str, str, int]]]):
        weighted_edges = len(edges[0]) == 3
        for edges in edges:
            if weighted_edges:
                self.add_edge(edges[0], edges[1], edges[2])
            else:
                self.add_edge(edges[0], edges[1])
        

    def add_vertex(self, vertex_name: str):
        self.vertices.add(vertex_name)

    def add_vertices(self, vertex_names: List[str]):
        for vertex in vertex_names:
            self.vertices.add(vertex)
