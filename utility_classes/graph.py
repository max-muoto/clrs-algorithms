from enum import Enum
from functools import cached_property
from typing import Dict, Optional, Set, List, Union, Tuple


class GraphType(Enum):
    UNDIRECTED_UNWEIGHTED = 1
    UNDIRECTED_WEIGHTED = 2
    DIRECTED_UNWEIGHTED = 3
    DIRECTED_WEIGHTED = 4


class Graph:
    vertex_adjacencies: Dict[str, Union[Dict[str, int], Set[str]]]
    edges: Union[List[Tuple[str, str]], List[Tuple[str, str, int]]]
    graph_type: GraphType

    def __init__(self, graph_type: GraphType):
        self.graph_type = graph_type
        self.vertex_adjacencies = {}
        self.edges = []

    @cached_property
    def is_directed_graph(self):
        return (
            self.graph_type == GraphType.DIRECTED_UNWEIGHTED
            or self.graph_type == GraphType.DIRECTED_WEIGHTED
        )

    @cached_property
    def is_weighted_graph(self):
        return (
            self.graph_type == GraphType.UNDIRECTED_WEIGHTED
            or self.graph_type == GraphType.DIRECTED_WEIGHTED
        )

    def add_edge(self, u: str, v: str, weight: Optional[int]):
        if weight and self.is_weighted_graph:
            self.vertex_adjacencies[u][v] = weight
            self.edges.append((u, v, weight))
            if not self.is_directed_graph:
                self.vertex_adjacencies[v][u] = weight
                self.edges.append((v, u, weight))
        elif not self.is_weighted_graph:
            self.vertex_adjacencies[u].add(v)
            self.edges.append((u, v))
            if not self.is_directed_graph:
                self.vertex_adjacencies[v].add(u)
                self.edges.append((v, u))
        else:
            raise ValueError(
                "You incorrectly set the weight corresponding to the graph's type."
            )

    def add_edges(
        self, edges: Union[List[Tuple[str, str]], List[Tuple[str, str, int]]]
    ):
        weighted_edges = len(edges[0]) == 3
        for edges in edges:
            if weighted_edges:
                self.add_edge(edges[0], edges[1], edges[2])
            else:
                self.add_edge(edges[0], edges[1])

    def add_vertex(self, vertex_name: str):
        if self.is_weighted_graph:
            self.vertex_adjacencies[vertex_name] = {}
        else:
            self.vertex_adjacencies[vertex_name] = set()

    def add_vertices(self, vertex_names: List[str]):
        for vertex in vertex_names:
            self.add_vertex(vertex)
