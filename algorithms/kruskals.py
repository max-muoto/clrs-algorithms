class DisjointForest:
    def __init__(self, p, val, rank):
        self.p = p
        self.val = val
        self.rank = rank


class KruskalsGraph:
    vertices = set()
    edges = []
    disjoint_forests = {}

    # Add undirected edge between two vertices
    def add_edge(self, node1, node2, weight):
        if node1 not in self.vertices:
            self.vertices.add(node1)
        if node2 not in self.vertices:
            self.vertices.add(node2)

        self.edges.append((node1, node2, weight))
        self.edges.append((node2, node1, weight))

    def kruskals(self):
        answer = set()

        for vertex in self.vertices:
            self.make_set(vertex)

        # Sort edges from least to greatest.
        self.edges.sort(key=lambda x: x[2])
        for edge in self.edges:
            if self.findset(edge[0]) != self.findset(edge[1]):
                answer = answer.union({(edge[0], edge[1])})
                self.union(edge[0], edge[1])

        return answer

    def make_set(self, vertex):
        self.disjoint_forests[vertex] = DisjointForest(
            p=vertex, val=vertex, rank=0)

    def findset(self, vertex):
        if vertex != self.disjoint_forests[vertex].p:
            self.disjoint_forests[vertex].p = self.findset(
                self.disjoint_forests[vertex].p)
        return self.disjoint_forests[vertex].p

    def union(self, x, y):
        return self.link(self.disjoint_forests[self.findset(x)], self.disjoint_forests[self.findset(y)])

    def link(self, x, y):
        if x.rank > y.rank:
            y.p = x.val
        else:
            x.p = y.val
            if x.rank == y.rank:
                y.rank += 1
