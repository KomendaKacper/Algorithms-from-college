class Edge:
    def __init__(self, capacity, is_residual=False):
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity if not is_residual else 0
        self.is_residual = is_residual

    def __repr__(self):
        return f"Pojemność: {self.capacity} Przepływ rzeczywisty: {self.flow} Przepływ resztowy: {self.residual} Krawędź rzeczywista: {self.is_residual}"

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, capacity):
        if self.adj_matrix[u][v] is None:
            self.adj_matrix[u][v] = Edge(capacity)
        else:
            self.adj_matrix[u][v].capacity += capacity

        if self.adj_matrix[v][u] is None:
            self.adj_matrix[v][u] = Edge(0, is_residual=True)

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def vertices(self):
        return range(self.size)

    def neighbours(self, vertex):
        neighbours_with_weights = []
        for i, edge in enumerate(self.adj_matrix[vertex]):
            if edge:
                neighbours_with_weights.append((i, edge.capacity))
        return neighbours_with_weights

    def dfs(self, s, t, visited=None, path=None):
        if visited is None:
            visited = [False] * self.size
        if path is None:
            path = []

        visited[s] = True
        path.append(s)

        if s == t:
            return path

        for ind, edge in enumerate(self.adj_matrix[s]):
            if edge and not visited[ind] and edge.residual > 0:
                result_path = self.dfs(ind, t, visited, path.copy())
                if result_path:
                    return result_path

        return None

    def fordFulkerson(self, s, t):
        max_flow = 0
        path = self.dfs(s, t)
        while path:
            path_flow = float("Inf")
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                path_flow = min(path_flow, self.adj_matrix[u][v].residual)

            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.adj_matrix[u][v].residual -= path_flow
                self.adj_matrix[v][u].residual += path_flow
                self.adj_matrix[u][v].flow += path_flow

            max_flow += path_flow
            path_names = [self.vertex_data[node] for node in path]
            print("Ścieżka:", " -> ".join(path_names), ", Przepływ:", path_flow)
            path = self.dfs(s, t)
        return max_flow


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end="; ")
        print()
    print("-------------------")

vertex_names = ['s', 'u', 'v', 't']
graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
g0 = Graph(len(vertex_names))

for i, name in enumerate(vertex_names):
    g0.add_vertex_data(i, name)

for edge in graf_0:
    u, v, capacity = edge
    u_index = vertex_names.index(u)
    v_index = vertex_names.index(v)
    g0.add_edge(u_index, v_index, capacity)

s = vertex_names.index('s')
t = vertex_names.index('t')

print ("Graf 0:")
print("Maksymalny przepływ: %d" % g0.fordFulkerson(s, t))
printGraph(g0)
print ()

graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14),
          ('d', 'b', 7), ('d', 't', 4)]
g1 = Graph(6)

vertex_names_g1 = ['s', 'a', 'b', 'c', 'd', 't']
for i, name in enumerate(vertex_names_g1):
    g1.add_vertex_data(i, name)

for edge in graf_1:
    u, v, capacity = edge
    u_index = vertex_names_g1.index(u)
    v_index = vertex_names_g1.index(v)
    g1.add_edge(u_index, v_index, capacity)

s = vertex_names_g1.index('s')
t = vertex_names_g1.index('t')

print ("Graf 1:")
print("Maksymalny przepływ: %d" % g1.fordFulkerson(s, t))
printGraph(g1)
print ()

graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
          ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
g2 = Graph(7)

vertex_names_g2 = ['s', 'a', 'b', 'c', 'd', 't', 'e']
for i, name in enumerate(vertex_names_g2):
    g2.add_vertex_data(i, name)

for edge in graf_2:
    u, v, capacity = edge
    u_index = vertex_names_g2.index(u)
    v_index = vertex_names_g2.index(v)
    g2.add_edge(u_index, v_index, capacity)

s = vertex_names_g2.index('s')
t = vertex_names_g2.index('t')

print ("Graf 2:")
print("Maksymalny przepływ: %d" % g2.fordFulkerson(s, t))
printGraph(g2)
