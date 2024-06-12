import numpy as np
import heapq
from copy import deepcopy
from math import inf

INF = float('inf')

def lb(matrix):
    reduction = 0
    
    min_row = np.min(matrix, axis=1, keepdims=True) # Znajdowanie minimalnych wartości w każdym wierszu macierzy
    min_row[min_row == inf] = 0     # Zamiana wartości nieskończoności na 0, aby nie wpływały na sumowanie
    reduction += np.sum(min_row)    # Dodanie sumy minimalnych wartości wierszy lb
    matrix -= min_row
    min_col = np.min(matrix, axis=0)
    min_col[min_col == inf] = 0
    reduction += np.sum(min_col)     # Dodawanie sumy minimalnych wartości kolumn do redukcji
    matrix -= min_col
    
    return reduction                 # Zwracanie całkowitej wartości redukcji


def generate_identifier():
    current_identifier = 0
    while True:
        yield current_identifier
        current_identifier += 1

# Inicjalizacja generatora identyfikatorów
id_generator = generate_identifier()

class Node:
    def __init__(self, reduced_matrix, lower_bound, path, criterion):
        self.id = next(id_generator)  # Przypisanie unikatowego identyfikatora
        self.reduced_matrix = reduced_matrix  # Zredukowana macierz kosztów
        self.lower_bound = lower_bound  # Dolne ograniczenie (LB)
        self.path = path  # Lista odcinków rozwiązania TSP (częściowego)
        self.criterion = criterion  # Kryterium zamykania (KZ)

    def __lt__(self, other):
        return self.lower_bound < other.lower_bound

def reduce_matrix(matrix):
    # Redukcja wierszy
    row_mins = matrix.min(axis=1)
    row_reduced = matrix - row_mins.reshape(-1, 1)

    # Redukcja kolumn
    col_mins = row_reduced.min(axis=0)
    col_reduced = row_reduced - col_mins

    # Obliczenie kosztu redukcji
    reduction_cost = np.sum(row_mins) + np.sum(col_mins)

    return col_reduced, reduction_cost

def create_child_node(parent, i, j):
    new_matrix = parent.reduced_matrix.copy()
    new_matrix[i, :] = np.inf
    new_matrix[:, j] = np.inf
    new_matrix[j, 0] = np.inf  # prevent returning to the starting node
    new_matrix[i, j] = np.inf

    reduced_matrix, reduction_cost = reduce_matrix(new_matrix)
    lower_bound = parent.lower_bound + parent.reduced_matrix[i, j] + reduction_cost
    path = parent.path + [(i, j)]  # Aktualizacja ścieżki
    lower_bound = lb(reduced_matrix)  # Obliczenie dolnego ograniczenia
    return Node(reduced_matrix, lower_bound, path, 'KZ0')  # Nowy węzeł z aktualizowaną ścieżką

def tsp_little_algorithm(cost_matrix):
    n = len(cost_matrix)
    initial_reduced_matrix, reduction_cost = reduce_matrix(cost_matrix)
    initial_lower_bound = reduction_cost

    initial_node = Node(initial_reduced_matrix, initial_lower_bound, [], 'KZ0')
    pq = [initial_node]
    heapq.heapify(pq)
    best_cost = np.inf
    best_path = []

    while pq:
        node = heapq.heappop(pq)

        # KZ1 - Zamknięcie podproblemu, jeśli dolne ograniczenie >= najlepsza znaleziona wartość
        if node.lower_bound >= best_cost:
            node.criterion = 'KZ1'
            continue

        # KZ2 - Zamknięcie podproblemu, jeśli ścieżka jest pełna
        if len(node.path) == n - 1:
            final_cost = node.lower_bound + cost_matrix[node.path[-1][1]][0]
            if final_cost < best_cost:
                best_cost = final_cost
                best_path = node.path + [(node.path[-1][1], 0)]
            node.criterion = 'KZ2'
            continue

        # Tworzenie dzieci (podział - KZ0)
        for j in range(1, n):
            if (node.path and node.path[-1][1] == j) or any(p[1] == j for p in node.path):
                continue
            child_node = create_child_node(node, node.path[-1][1] if node.path else 0, j)
            if child_node.lower_bound < best_cost:
                heapq.heappush(pq, child_node)
            else:
                child_node.criterion = 'KZ3'  # KZ3 - Inne warunki zamknięcia

    return best_cost, best_path

M =  np.array([ 
    [np.inf, 5, 4, 6, 6], 
    [8, np.inf, 5, 3, 4], 
    [4, 3, np.inf, 3, 1], 
    [8, 2, 5, np.inf, 6], 
    [2, 2, 7, 0, np.inf]])


print(tsp_little_algorithm(M))