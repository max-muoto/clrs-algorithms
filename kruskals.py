class DisjointForest:
    def __init__(self, p, val, rank):
        self.p = p
        self.val = val
        self.rank = rank


class Edge:
    u = None
    v = None
    weight = None

    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


class Graph:
    vertices = set()
    edges = set()
    disjoint_forests = {}

    # Add undirected edge between two vertices
    def add_edge(self, node1, node2, weight):
        if node1 not in self.vertices:
            self.vertices.add(node1)
        if node2 not in self.vertices:
            self.vertices.add(node2)

        self.edges.add(Edge(node1, node2, weight))
        self.edges.add(Edge(node2, node1, weight))

    def kruskals(self, root):
        answer = set()

        for vertex in self.vertices:
            self.make_set(vertex)

        # Sort edges from least to greatest.
        self.edges = sorted(self.edges, key=lambda x: x.weight)

        for edge in self.edges:
            if self.findset(edge.u) != self.findset(edge.v):
                answer = answer.union({(edge.u, edge.v)})
                self.union(edge.u, edge.v)

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


def main():
    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 3)
    graph.add_edge("A", "D", 3)
    graph.add_edge("C", "D", 2)
    graph.add_edge("B", "C", 4)
    graph.add_edge("E", "B", 3)
    graph.add_edge("C", "E", 1)
    graph.add_edge("D", "E", 3)
    graph.add_edge("F", "E", 2)
    graph.add_edge("F", "C", 9)
    print("MST is: ", graph.kruskals("A"))


if __name__ == "__main__":
    main()
