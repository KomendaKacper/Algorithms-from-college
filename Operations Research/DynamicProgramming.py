import numpy as np

def calculate_costs(g, h, q, y_min, y_max, y_n):
    num_states = y_max - y_min + 1  # Liczba możliwych stanów
    num_steps = len(q)  # Liczba kroków

    res = np.zeros((num_states, num_steps))  # Inicjalizacja macierzy decyzji
    
    cost_matrix = np.full((num_states, num_steps), np.inf)  # Inicjalizacja macierzy kosztów, wypełniona wartościami nieskończonymi
    y = np.arange(y_min, y_max + 1)  # Tablica stanów od y_min do y_max

    # Przeglądanie każdego kroku (od ostatniego do pierwszego)
    for j in range(num_steps):
        for i in range(num_states):
            idx = num_steps - j - 1  # Indeks kroku w odwrotnej kolejności
            current_y = y[i]  # Aktualny stan

            # Wyznaczenie zakresu wartości x
            if j == 0:
                x_range = [y_n + q[idx] - current_y]
            else:
                x_min = max(y_min + q[idx] - current_y, 0)
                x_max = min(y_max + q[idx] - current_y, len(g) - 1)
                x_range = range(x_min, x_max + 1)

            # Przeglądanie możliwych wartości x
            for x in x_range:
                if 0 <= x < len(g):
                    if j == 0:
                        cost = g[x]  # Koszt dla pierwszego kroku
                    else:
                        # Koszt dla pozostałych kroków
                        cost = g[x] + h[current_y + x - q[idx] - y_min] + cost_matrix[current_y + x - q[idx] - y_min, j - 1]

                    # Aktualizacja macierzy kosztów i decyzji
                    if cost < cost_matrix[i, j]:
                        res[i, j] = x
                        cost_matrix[i, j] = cost

    return res, cost_matrix

def print_results(q, y_min, y_0, res, cost_matrix):
    # Inicjalizacja wyniku z całkowitym kosztem
    result = f"Koszt całkowity = {cost_matrix[y_0 - y_min, -1]}\n"
    result += "------------------------\n"
    
    state = y_0
    
    # Rekonstrukcja decyzji w odwrotnej kolejności
    for j in range(cost_matrix.shape[1] - 1, -1, -1):
        idx = cost_matrix.shape[1] - j - 1
        decision = int(res[state - y_min, j])
        result += f"y{idx} = {state}, x{idx + 1} = {decision}\n"
        state = state + decision - q[idx]  # Aktualizacja stanu magazynu
    result += f"y{idx+1} = {state}"

    # Wypisanie macierzy decyzji i kosztów
    result += "\nMacierz decyzji:\n"
    result += str(res)
    result += "\n\nMacierz kosztów:\n"
    result += str(cost_matrix)
    return result

# Dane wejściowe
g = np.array([0, 15, 18, 19, 20, 24])  # Koszty produkcji
h = np.array([i * 2 for i in range(6)])  # Koszt magazynowania
q = np.array([3, 3, 3, 3, 3, 3])  # Wymagane ilości produktu
y_min = 0  # Minimalna pojemność magazynu
y_max = 4  # Maksymalna pojemność magazynu
y_0 = 0  # Początkowy stan magazynu
y_n = 0  # Końcowy stan magazynu

# Obliczenia
res, cost_matrix = calculate_costs(g, h, q, y_min, y_max, y_n)
results = print_results(q, y_min, y_0, res, cost_matrix)

# Wyświetlenie wyników
print(results)

print ()

g2 = np.array([0, 21, 43, 55, 60, 86, 93, 120, 133])  
h2 = np.array([0, 1, 3, 7, 10, 15, 20, 23, 24])  
q2 = np.array([5, 3, 8, 6, 7, 13, 5, 6, 7, 10, 10, 9])  
y_min2 = 0 
y_max2 = 8
y_02 = 0  
y_end2 = 0

res2, cost_matrix2 = calculate_costs(g2, h2, q2, y_min2, y_max2, y_end2)
results2 = print_results(q2, y_min2, y_02, res2, cost_matrix2)

print(results2)
