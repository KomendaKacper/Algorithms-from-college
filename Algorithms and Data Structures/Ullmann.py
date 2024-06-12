import numpy as np
from copy import deepcopy

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:
            return True
        
    def __hash__(self):
        return hash(self.key)
    
    def __str__(self):
        return str(self.key)
    
    def __repr__(self):
        return repr(self.key)

class MatrixGraph:
    def __init__(self, val=0):
        self.graph_list = []
        self.neighbours_matrix = []
        self.val = val

    def get_vertex_id(self, vertex):
        for i in range(len(self.graph_list)):
            if self.graph_list[i] == vertex:
                return i
        return None
    
    def get_vertex(self, vertex_id):
        return self.graph_list[vertex_id]
    
    def is_empty(self):
        return self.graph_list == []
    
    def insert_vertex(self, vertex):
        if vertex not in self.graph_list:
            self.graph_list.append(vertex)
            size = len(self.graph_list)
            for row in self.neighbours_matrix:
                row.append(self.val)
            self.neighbours_matrix.append([self.val] * size)

    def insert_edge(self, vertex1, vertex2, edge=1):
        idx1 = self.get_vertex_id(vertex1)
        idx2 = self.get_vertex_id(vertex2)
        
        self.neighbours_matrix[idx1][idx2] = edge
        self.neighbours_matrix[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        idx = self.get_vertex_id(vertex)
        if idx is not None:
            del self.graph_list[idx]
            del self.neighbours_matrix[idx]
            for row in self.neighbours_matrix:
                del row[idx]
    
    def delete_edge(self, vertex1, vertex2):
        idx1 = self.get_vertex_id(vertex1)
        idx2 = self.get_vertex_id(vertex2)
    
        if idx1 != None and idx2 != None:
            self.neighbours_matrix[idx1][idx2] = self.val
            self.neighbours_matrix[idx2][idx1] = self.val
            
    def __str__(self):
        res = ""
        for e in self.graph_list:
            res += str(e) + ", "
        return res[:-2]
    
    def neighbours(self, vertex_id, edge = 1):
        res = []
        for idx, vertex in enumerate(self.neighbours_matrix[vertex_id]):
            if vertex != 0:
                res.append((idx, edge))
        return res

    def vertices(self):
        res = []
        for i in range(len(self.graph_list)):
            res.append(i)
        return res
    
def ullmann_1(cols_used, curr_row, M, G, P, calls=0, isomorphisms=0):
    calls += 1
    rows, cols = M.shape

    if curr_row == rows:
        if (P == (M @ np.transpose(M @ G))).all():
            isomorphisms += 1
        return calls, isomorphisms
    
    for c in range(cols):
        if c not in cols_used:
            for i in range(cols):
                M[curr_row][i] = 0
            M[curr_row][c] = 1

            cols_used.append(c)
            calls, isomorphisms = ullmann_1(cols_used, curr_row + 1, M, G, P, calls, isomorphisms)
            cols_used.remove(c)

    return calls, isomorphisms

def ullmann_2(cols_used, curr_row, M, G, P, M0, calls=0, isomorphisms=0):
    calls += 1
    rows, cols = M.shape

    if curr_row == rows:
        if (P == (M @ np.transpose(M @ G))).all():
            isomorphisms += 1
        return calls, isomorphisms

    for c in range(cols):
        if c not in cols_used and M0[curr_row][c] != 0:
            Mcopy = deepcopy(M)
            for i in range(cols):
                Mcopy[curr_row][i] = 0
            Mcopy[curr_row][c] = 1

            cols_used.append(c)
            calls, isomorphisms = ullmann_2(cols_used, curr_row + 1, Mcopy, G, P, M0, calls, isomorphisms)
            cols_used.remove(c)

    return calls, isomorphisms

def prune(M):
    rows, cols = M.shape
    while True:
        for i in range(rows):
            for j in range(cols):
                if M[i, j] == 1:
                    neigh_exist = any(M[x, y] == 1 for x in range(rows) for y in range(cols) if x == i or y == j)
                    if not neigh_exist:
                        M[i, j] = 0
                    else:
                        return

def ullmann_3(cols_used, curr_row, M, G, P, M0, calls=0, isomorphisms=0):
    calls += 1
    rows, cols = M.shape

    if curr_row == rows:
        if (P == (M @ np.transpose(M @ G))).all():
            isomorphisms += 1
        return calls, isomorphisms

    Mcopy = deepcopy(M)
    prune(Mcopy)

    for c in range(cols):
        if c not in cols_used and M0[curr_row][c] != 0:
            Mcopy = deepcopy(M)
            for i in range(cols):
                Mcopy[curr_row][i] = 0
            Mcopy[curr_row][c] = 1

            cols_used.append(c)
            calls, isomorphisms = ullmann_3(cols_used, curr_row + 1, Mcopy, G, P, M0, calls, isomorphisms)
            cols_used.remove(c)

    return calls, isomorphisms

if __name__ == '__main__':
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    g1 = MatrixGraph()
    g2 = MatrixGraph()

    for v in graph_G:
        if Vertex(v[0]) not in g1.graph_list:
            g1.insert_vertex(Vertex(v[0]))
        if Vertex(v[1]) not in g1.graph_list:
            g1.insert_vertex(Vertex(v[1]))
        g1.insert_edge(Vertex(v[0]), Vertex(v[1]))

    for v in graph_P:
        if Vertex(v[0]) not in g2.graph_list:
            g2.insert_vertex(Vertex(v[0]))
        if Vertex(v[1]) not in g2.graph_list:
            g2.insert_vertex(Vertex(v[1]))
        g2.insert_edge(Vertex(v[0]), Vertex(v[1]))

    G = np.array(g1.neighbours_matrix)
    P = np.array(g2.neighbours_matrix)
    M = np.zeros((len(P), len(G)))

    M0 = np.zeros((len(M), len(M[0])))
    
    for i in range(len(P)):
        degvi = np.count_nonzero(P[i, :])
        for j in range(len(G)):
            degvj = np.count_nonzero(G[j, :])
            if degvi <= degvj:
                M0[i, j] = 1

    calls1, isomorphisms1 = ullmann_1([], 0, M, G, P)
    print("Wyniki dla algorytmu ullmanna 1.0:")
    print(f"Liczba wywołań rekurencyjnych: {calls1}, Liczba znalezionych izomorfizmów: {isomorphisms1}")

    calls2, isomorphisms2 = ullmann_2([], 0, M, G, P, M0)
    print("\nWyniki dla algorytmu ullmanna 2.0:")
    print(f"Liczba wywołań rekurencyjnych: {calls2}, Liczba znalezionych izomorfizmów: {isomorphisms2}")

    calls3, isomorphisms3 = ullmann_3([], 0, M, G, P, M0)
    print("\nWyniki dla algorytmu ullmanna 3.0:")
    print(f"Liczba wywołań rekurencyjnych: {calls3}, Liczba znalezionych izomorfizmów: {isomorphisms3}")
