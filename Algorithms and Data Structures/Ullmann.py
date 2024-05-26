import numpy as np

def create_adjacency_matrix(edges, num_vertices):
    matrix = np.zeros((num_vertices, num_vertices))
    for (u, v, w) in edges:
        i = ord(u) - ord('A')
        j = ord(v) - ord('A')
        matrix[i, j] = w
        matrix[j, i] = w
    return matrix

def ullmann(used_columns, current_row, M, P, G, valid_matrices, call_count):
    num_rows = M.shape[0]
    num_cols = M.shape[1]

    if current_row == num_rows:
        if np.array_equal(P, M @ G @ M.T):
            valid_matrices.append(M.copy())
        return call_count + 1

    for c in range(num_cols):
        if not used_columns[c]:
            used_columns[c] = True
            M[current_row, :] = 0
            M[current_row, c] = 1
            call_count = ullmann(used_columns, current_row + 1, M, P, G, valid_matrices, call_count)
            used_columns[c] = False

    return call_count

def find_isomorphisms(P, G):
    num_rows = P.shape[0]
    num_cols = G.shape[0]
    M = np.zeros((num_rows, num_cols))
    used_columns = [False] * num_cols
    valid_matrices = []
    call_count = ullmann(used_columns, 0, M, P, G, valid_matrices, 0)
    return valid_matrices, call_count

def create_M0(P, G):
    num_rows = P.shape[0]
    num_cols = G.shape[0]
    M0 = np.ones((num_rows, num_cols))
    deg_P = np.sum(P, axis=1)
    deg_G = np.sum(G, axis=1)
    for i in range(num_rows):
        for j in range(num_cols):
            if deg_P[i] > deg_G[j]:
                M0[i, j] = 0
    return M0

def ullmann_v2(used_columns, current_row, M, M0, P, G, valid_matrices, call_count):
    num_rows = M.shape[0]
    num_cols = M.shape[1]

    if current_row == num_rows:
        if np.array_equal(P, M @ G @ M.T):
            valid_matrices.append(M.copy())
        return call_count + 1

    for c in range(num_cols):
        if not used_columns[c] and M0[current_row, c] == 1:
            used_columns[c] = True
            M[current_row, :] = 0
            M[current_row, c] = 1
            call_count = ullmann_v2(used_columns, current_row + 1, M, M0, P, G, valid_matrices, call_count)
            used_columns[c] = False

    return call_count

def find_isomorphisms_v2(P, G):
    num_rows = P.shape[0]
    num_cols = G.shape[0]
    M0 = create_M0(P, G)
    M = np.zeros((num_rows, num_cols))
    used_columns = [False] * num_cols
    valid_matrices = []
    call_count = ullmann_v2(used_columns, 0, M, M0, P, G, valid_matrices, 0)
    return valid_matrices, call_count

def prune(M, P, G):
    changed = True
    while changed:
        changed = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j] == 1:
                    neighbors_P = np.where(P[i, :] == 1)[0]
                    neighbors_G = np.where(G[j, :] == 1)[0]
                    if not any([M[x, y] == 1 for x in neighbors_P for y in neighbors_G]):
                        M[i, j] = 0
                        changed = True
    return M

def ullmann_v3(used_columns, current_row, M, M0, P, G, valid_matrices, call_count):
    num_rows = M.shape[0]
    num_cols = M.shape[1]

    if current_row == num_rows:
        if np.array_equal(P, M @ G @ M.T):
            valid_matrices.append(M.copy())
        return call_count + 1

    for c in range(num_cols):
        if not used_columns[c] and M0[current_row, c] == 1:
            used_columns[c] = True
            M[current_row, :] = 0
            M[current_row, c] = 1
            M = prune(M.copy(), P, G)
            call_count = ullmann_v3(used_columns, current_row + 1, M, M0, P, G, valid_matrices, call_count)
            used_columns[c] = False

    return call_count

def find_isomorphisms_v3(P, G):
    num_rows = P.shape[0]
    num_cols = G.shape[0]
    M0 = create_M0(P, G)
    M = np.zeros((num_rows, num_cols))
    used_columns = [False] * num_cols
    valid_matrices = []
    call_count = ullmann_v3(used_columns, 0, M, M0, P, G, valid_matrices, 0)
    return valid_matrices, call_count

graph_G_edges = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
graph_P_edges = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
num_vertices_G = 6
num_vertices_P = 3
G = create_adjacency_matrix(graph_G_edges, num_vertices_G)
P = create_adjacency_matrix(graph_P_edges, num_vertices_P)

print("Macierz sąsiedztwa grafu G:")
print(G)
print("\nMacierz sąsiedztwa grafu P:")
print(P)

valid_matrices, call_count = find_isomorphisms(P, G)

valid_matrices_v2, call_count_v2 = find_isomorphisms_v2(P, G)

valid_matrices_v3, call_count_v3 = find_isomorphisms_v3(P, G)

print("Liczba znalezionych izomorfizmów (wersja 1.0):", len(valid_matrices))
print("Liczba wywołań rekurencyjnych (wersja 1.0):", call_count)

print("Liczba znalezionych izomorfizmów (wersja 2.0):", len(valid_matrices_v2))
print("Liczba wywołań rekurencyjnych (wersja 2.0):", call_count_v2)

print("Liczba znalezionych izomorfizmów (wersja 3.0):", len(valid_matrices_v3))
print("Liczba wywołań rekurencyjnych (wersja 3.0):", call_count_v3)
