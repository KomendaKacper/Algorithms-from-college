from math import inf

def DPA(G, wagi, s):
    suma = 0 # suma wag
    A = [] 
    V = list(G.keys()) # lista indeksów wierzchołków

    alfa = [0 for _ in range(max(V) + 1)] # ustawienie indeksów poprzedników na 0 
    beta = [inf for _ in range(max(V) + 1)] # ustawienie wag na nieskończoność

    Q = V # lista nieodwiedzonych wierzchołków
    beta[s] = 0 # odległość pierwszego wierzchołka od niego samego

    Q.remove(s)
    ul = s
    # usuwam z nieodwiedzonych wierzchołków pierwszy element i ustawiam go na poprzednika

    while Q: # póki mamy nieodwiedzone wierzchołki
        for el in Q:  # dla każdego u należącego do Q
            for u in G[ul]:
                if weight(wagi, u, ul) < beta[u]:
                    alfa[u] = ul
                    beta[u] = weight(wagi, u, ul)
        # Szukamy wagi krawędzi między sąsiadami mniejszej niż aktualna. 

        min = inf
        for u in Q:
            if beta[u] < min:
                min = beta[u]
                ul = u
        # Wybieramy wierzchołek o najmniejszej wadze z listy Q

        Q.remove(ul)
        A.append([alfa[ul], ul])
        suma += weight(wagi, ul, alfa[ul])  # Dodajemy wagę krawędzi do sumy

    return A, suma #Zwracam minimalne drzewo rozpinające wraz z sumą wag krawędzi




wagi = [
    [inf, 2, 4, 5, inf, inf, inf, inf, inf, inf],
    [2, inf, 1, 4, 3, inf, inf, inf, inf, inf],
    [4, 1, inf, 2, 5, inf, inf, inf, inf, inf],
    [5, 4, 2, inf, 4, inf, inf, inf, inf, inf],
    [inf, 3, 5, 4, inf, 7, inf, inf, inf, inf],
    [inf, inf, inf, inf, 7, inf, 2, 4, 1, inf],
    [inf, inf, inf, inf, inf, 2, inf, 1, 5, 5],
    [inf, inf, inf, inf, inf, 4, 1, inf, 2, 3],
    [inf, inf, inf, inf, inf, 1, 5, 2, inf, 6],
    [inf, inf, inf, inf, inf, inf, 5, 3, 6, inf]
]

def weight(wagi, u, v):
    return wagi[u - 1][v - 1] #funkcja zwracająca wagi krawędzi z macierzy


graph = {
    1: [2, 3, 4],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [1, 2, 3, 5],
    5: [2, 3, 4, 6],
    6: [5, 7, 8, 9],
    7: [6, 8, 9, 10],
    8: [6, 7, 9, 10],
    9: [6, 7, 8, 10],
    10: [7, 8, 9]
}

print(DPA(graph, wagi, 1))
