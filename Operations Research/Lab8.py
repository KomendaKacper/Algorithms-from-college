import numpy as np

def znajdz_zerowy_element(zero_mat):
    mark_zero = []
    # Iterujemy, dopóki istnieją zera w macierzy
    while np.count_nonzero(zero_mat) > 0:
        min_row = [99999, -1]

        # Znajdujemy wiersz z najmniejszą ilością zer
        for row_num in range(zero_mat.shape[0]):
            count_zeros = np.sum(zero_mat[row_num] == 0)
            if count_zeros > 0 and min_row[0] > count_zeros:
                min_row = [count_zeros, row_num]

        # Jeśli znajdujemy wiersz z zerami
        if min_row[1] != -1:
            zero_index = np.where(zero_mat[min_row[1]] == 0)[0][0]
            mark_zero.append((min_row[1], zero_index))
            # Oznaczamy wiersz i kolumnę zawierającą zero jako użyte
            zero_mat[min_row[1], :] = True
            zero_mat[:, zero_index] = True
        else:
            break  # Jeśli nie ma już zer do wyznaczenia, przerywamy pętlę
        
    return mark_zero

def adjust_matrix(mat, cover_rows, cover_cols):
    cur_mat = np.copy(mat)
    non_zero_elements = []

    # Znajdujemy najmniejszą wartość elementu nieoznaczonego w zaznaczonych wierszach/kolumnach
    for row in range(cur_mat.shape[0]):
        if row not in cover_rows:
            for col in range(cur_mat.shape[1]):
                if col not in cover_cols:
                    non_zero_elements.append(cur_mat[row, col])

    min_num = min(non_zero_elements)

    # Odejmujemy od wszystkich wartości nieoznaczonych wierszy/kolumn
    for row in range(cur_mat.shape[0]):
        if row not in cover_rows:
            for col in range(cur_mat.shape[1]):
                if col not in cover_cols:
                    cur_mat[row, col] -= min_num

    # Dodajemy do wszystkich wartości oznaczonych wierszy/kolumn
    for row in cover_rows:
        for col in cover_cols:
            cur_mat[row, col] += min_num

    return cur_mat

# Przykładowa macierz
mat = np.array([[0,0,0,1], [3,0,4,1], [9,4,0,0], [1,0,1,7]])

# Przykładowe zaznaczone wiersze i kolumny
cover_rows = [0, 2]
cover_cols = [1]

print("Macierz początkowa:")
print(mat)

# Dostosowujemy macierz do wyznaczonych zer niezależnych
adjusted_mat = adjust_matrix(mat, cover_rows, cover_cols)
print("\nMacierz po dostosowaniu liczby zer niezależnych:")
print(adjusted_mat)

# Wyznaczamy i wypisujemy pozycje zer niezależnych
print("\nWiersze i kolumny zer niezależnych:")
print(znajdz_zerowy_element(adjusted_mat))
