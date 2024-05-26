from collections import deque


class Edge:
    def __init__(self, capacity, is_residual=False):
        self.capacity = capacity
        self.flow = 0
        self.residual = capacity if not is_residual else 0
        self.is_residual = is_residual

    def __repr__(self):
        return f"Pojemność: {self.capacity} Przepływ rzeczywisty: {self.flow} Przepływ resztowy: {self.residual} Krawędź resztowa: {self.is_residual}"

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

    def bfs(self, s, t):
        visited = [False] * self.size
        parent = [-1] * self.size
        queue = deque()

        visited[s] = True
        queue.append(s)

        while queue:
            u = queue.popleft()

            for v, edge_capacity in self.neighbours(u):
                if not visited[v] and self.adj_matrix[u][v].residual > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)

        return parent
    
    def find_path_flow(self, parent):
        current_vertex = self.size - 1
        min_residual_flow = float("inf")

        if parent[current_vertex] == -1:
            return 0
        
        while current_vertex != 0:
            u = parent[current_vertex]
            v = current_vertex
            residual_flow = self.adj_matrix[u][v].residual
            min_residual_flow = min(min_residual_flow, residual_flow)
            current_vertex = u

        return min_residual_flow


    def augment_path(self, parent, t, min_flow):
        current_vertex = t
        while parent[current_vertex] != -1:
            u = parent[current_vertex]
            v = current_vertex
            edge = self.adj_matrix[u][v]
            if not edge.is_residual:
                edge.flow += min_flow
                edge.residual -= min_flow
                reverse_edge = self.adj_matrix[v][u]
                reverse_edge.residual += min_flow
            else:
                edge.residual -= min_flow
                reverse_edge = self.adj_matrix[v][u]
                reverse_edge.flow -= min_flow
            current_vertex = u

    def fordFulkerson(self, s, t):
        parent = self.bfs(s, t)
        max_flow = 0
        while parent[t] != -1:
            path_flow = self.find_path_flow(parent)
            self.augment_path(parent, t, path_flow)
            max_flow += path_flow
            parent = self.bfs(s, t)
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

graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

g2 = Graph(7)

vertex_names_g2 = ['s', 'a', 'b', 'c', 'd', 'e', 't']
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