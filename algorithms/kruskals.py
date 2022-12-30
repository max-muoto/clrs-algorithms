from utility_classes.graph import Graph


class DisjointForest:
    def __init__(self, p, val, rank):
        self.p = p
        self.val = val
        self.rank = rank


class Kruskals:
    disjoint_forests = {}

    def minimum_spanning_tree(self, graph: Graph):
        answer = set()
        adj_vertices = graph.vertex_adjacencies
        edges = graph.edges

        for vertex in adj_vertices:
            self.make_set(vertex)

        # Sort edges from least to greatest in terms of weight.
        edges.sort(key=lambda edge: edge[2])

        for edge in edges:
            if self.findset(edge[0]) != self.findset(edge[1]):
                answer = answer.union({(edge[0], edge[1])})
                self.union(edge[0], edge[1])

        return answer

    def make_set(self, vertex):
        self.disjoint_forests[vertex] = DisjointForest(p=vertex, val=vertex, rank=0)

    def findset(self, vertex):
        if vertex != self.disjoint_forests[vertex].p:
            self.disjoint_forests[vertex].p = self.findset(
                self.disjoint_forests[vertex].p
            )
        return self.disjoint_forests[vertex].p

    def union(self, x, y):
        return self.link(
            self.disjoint_forests[self.findset(x)],
            self.disjoint_forests[self.findset(y)],
        )

    def link(self, x, y):
        if x.rank > y.rank:
            y.p = x.val
        else:
            x.p = y.val
            if x.rank == y.rank:
                y.rank += 1
