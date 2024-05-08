def plecak(W, wagi, wartosci, n):
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

    return K[n][W]

# Przykładowe dane wejściowe
wartosci = [60, 100, 120, 200, 300, 400, 150, 180, 220, 250]  # Wartości przedmiotów
wagi = [10, 20, 30, 25, 15, 35, 40, 22, 18, 29]                # Wagi przedmiotów
W = 100                                                       # Pojemność plecaka
n = len(wartosci)                                             # Liczba przedmiotów

# Wyświetlenie maksymalnego możliwego zysku
print(plecak(W, wagi, wartosci, n))
