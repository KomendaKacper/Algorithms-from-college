import numpy as np

def johnson(m):
    # Redukcja macierzy: obliczenie sum czasów trwania zadań dla kolejnych par
    reduced = []
    for i in range(len(m) - 1):
        t = [x + y for x, y in zip(m[i], m[i+1])]
        reduced.append(t)
    
    matrix = reduced

    # Inicjalizacja tablicy przechowującej kolejność zadań
    order = np.zeros(len(matrix[0]), dtype=int)
    # Lista przechowująca indeksy odwiedzonych zadań
    visited = []
    # Licznik dla zadań dodawanych na lewą stronę kolejności
    l = 0
    # Licznik dla zadań dodawanych na prawą stronę kolejności
    r = -1

    # Algorytm Johnsona
    while len(visited) != len(matrix[0]):  # Dopóki nie odwiedzono wszystkich zadań
        min_val = np.inf  # Inicjalizacja minimalnej wartości jako nieskończoność
        pos = None  # Zmienna przechowująca pozycję minimalnej wartości
        
        # Szukanie minimalnej wartości w zredukowanej macierzy
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min_val and j not in visited:
                    # Sprawdzenie warunków minimalności wartości
                    if i == 0:
                        # Dla wiersza 0: sprawdzamy, czy poprzednie zadanie na drugiej maszynie jest mniejsze niż obecne
                        if visited and matrix[1][j] <= matrix[0][visited[-1]]:
                            min_val = matrix[i][j]
                            pos = (i, j)
                    else:
                        # Dla wiersza 1: sprawdzamy, czy poprzednie zadanie na pierwszej maszynie jest mniejsze niż obecne
                        if visited and matrix[0][j] <= matrix[1][visited[0]]:
                            min_val = matrix[i][j]
                            pos = (i, j)
                elif matrix[i][j] < min_val and j not in visited:
                    min_val = matrix[i][j]
                    pos = (i, j)
        
        visited.append(pos[1])  # Dodanie indeksu odwiedzonego zadania
        
        # Aktualizacja tablicy przechowującej kolejność zadań
        if pos[0] == 0:
            order[l] = pos[1]
            l += 1
        else:
            order[r] = pos[1]
            r -= 1

    # Znajdź uszeregowanie początkowe
    start_order = order.copy()
    start_times = np.zeros(len(start_order))  # Inicjalizacja tablicy przechowującej czasy rozpoczęcia zadań dla każdej maszyny

    # Obliczenia dla czasów rozpoczęcia zadań dla każdej maszyny
    for i, task in enumerate(start_order):
        if i == 0:
            start_times[i] = m[0][task]  # Czas rozpoczęcia pierwszego zadania na pierwszej maszynie
        else:
            start_times[i] = start_times[i-1] + m[0][task]  # Czas rozpoczęcia kolejnych zadań na pierwszej maszynie

    # Oblicz czasy dla poszczególnych maszyn
    machine_times = []
    for j, row in enumerate (m):
        machine_time = []
        time = 0
        for i, elem in enumerate (start_order):
            if j != 0:
                time = row[elem] + machine_times[j-1][i]
            else:
                time += row[elem]
            machine_time.append(time)

        machine_times.append(machine_time)

    # Obliczenia dla czasów przestoju dla poszczególnych maszyn
    idle_times = []
    total_elapsed_time = max(machine_times[-1])  # Całkowity czas zakończenia zadań
    for i in range (3):
        if i == 0:
            idle_times.append(total_elapsed_time - machine_times[0][-1])  # Czas przestoju dla pierwszej maszyny
        else:
            idle_time = 0
            # Jeżeli nie jesteśmy na pierwszej maszynie
            if i != 0:
                idle_time += machine_times[i-1][0]  # Dodajemy czas rozpoczęcia pierwszego zadania dla maszyny 'i'
                for j in range(len(machine_times[0])-1):
                    idle_time += (machine_times[i-1][j+1] - machine_times[i][j])  # Dodajemy czas przestoju
                if i != 2:
                    idle_time += (machine_times[i+1][-1] - machine_times[i][-1])  # Dodajemy czas przestoju między zadaniami
            idle_times.append(idle_time)
    
    total_idle_time = sum(idle_times)  # Sumujemy czasy przestoju dla wszystkich maszyn

    # Obliczenie czasów zakończenia zadań dla poszczególnych maszyn
    end_times = [max(times) for times in machine_times]

    return start_order, machine_times, idle_times, total_idle_time, end_times

# Przykładowa macierz czasów trwania zadań dla 10 zadań na 3 maszynach
matrix = [
    [8, 10, 6, 7, 11, 9, 5, 4, 3, 2], 
    [5, 6, 2, 3, 4, 7, 8, 9, 10, 11], 
    [4, 9, 8, 6, 5, 1, 2, 3, 4, 5]
]

start_order, machine_times, idle_times, total_idle_time, end_times = johnson(matrix)
print("Uszeregowanie początkowe:", start_order)
print("Czasy dla poszczególnych maszyn:", machine_times)
print("Czasy przestoju dla poszczególnych maszyn:", idle_times)
print("Całkowity czas przestoju dla wszystkich maszyn:", total_idle_time)
print("Czasy zakończenia zadań dla poszczególnych maszyn:", end_times)
