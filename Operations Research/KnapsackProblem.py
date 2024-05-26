def plecak(W, wagi, wartosci):
    n = len(wartosci)
    # Inicjalizacja tablicy K zerami
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
            # Jeśli waga aktualnego przedmiotu jest większa niż pozostała pojemność, należy pominąć przedmiot
            else:
                K[i][w] = K[i-1][w]

    # Wyznaczanie wybranych przedmiotów
    wybrane_przedmioty = []
    i, j = n, W
    while i > 0 and j > 0:
        if K[i][j] != K[i - 1][j]:
            wybrane_przedmioty.append(i-1)
            j -= wagi[i - 1]
        i -= 1

    return K, K[n][W], wybrane_przedmioty

wartosci = [2,2,4,5,3,6,2,4,6,2]
wagi = [3,1,3,4,2,4,2,1,4,6]
W = 10 

matrix, res, items = plecak(W, wagi, wartosci)

print("Macierz decyzji optymalnych:")
for e in matrix:
    print(e)

print("\nMaksymalny możliwy zysk:", res)
print("Przedmioty wybrane do plecaka:")
for idx in items:
    print(f"Przedmiot {idx+1} (wartość: {wartosci[idx]}, waga: {wagi[idx]})")
