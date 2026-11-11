class EdgeList(list):
    def __init__(self):
        self.graph = []

    def append(self, vertex_from, vertex_to, weight):
        if vertex_to < vertex_from:
            vertex_from, vertex_to = vertex_to, vertex_from
        self.graph.append((weight, vertex_from, vertex_to))
        self.graph.sort()

    def __len__(self):
        return len(self.graph)

    def __repr__(self):
        return str(self.graph)

    def __eq__(self, other):
        return self.graph == other.graph


e1 = EdgeList()
e2 = EdgeList()

print(f"{(e1==e2)=}")
