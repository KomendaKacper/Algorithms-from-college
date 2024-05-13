def plecak(W, wagi, wartosci):
    n = len(wartosci)     
    # Inicjalizacja tablicy K z wartościami zerowymi
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Wypełnianie tablicy K algorytmem dynamicznym
    for i in range(n + 1):
        for w in range(W + 1):
            # Jeśli brak przedmiotów lub pojemność plecaka wynosi 0, zysk wynosi 0
            if i == 0 or w == 0:
                K[i][w] = 0
            # Jeśli waga aktualnego przedmiotu jest mniejsza lub równa pozostałej pojemności, rozważ jego dodanie lub pominięcie
            elif wagi[i-1] <= w:
                K[i][w] = max(wartosci[i-1] + K[i-1][w-wagi[i-1]], K[i-1][w])
            # Jeśli waga aktualnego przedmiotu jest większa niż pozostała pojemność, pominię przedmiot
            else:
                K[i][w] = K[i-1][w]

    return K, K[n][W]

wartosci = [10,15,40]
wagi = [1,2,3]
W = 6      # Pojemność plecaka

# Wyświetlenie maksymalnego możliwego zysku
matrix, res = plecak(W, wagi, wartosci)

print("Macierz decyzji optymalnych:")
for e in matrix:
    print(e)

print("\nWartość funkcji dla każdego etapu i rozważanego stanu:")
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"K[{i}][{j}] = {val}")

print("\nMaksymalny możliwy zysk:", res)
