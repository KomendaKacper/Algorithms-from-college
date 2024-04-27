import sys

# Liczba wierzchołków w grafie
V = 4

# Funkcja pomocnicza do znalezienia wierzchołka z najmniejszą odległością
def minDistance(dist, sptSet):
    min_val = sys.maxsize
    min_index = 0
 
    for v in range(V):
        if sptSet[v] == False and dist[v] <= min_val:
            min_val = dist[v]
            min_index = v
 
    return min_index 

# Funkcja do wyświetlania macierzy odległości
def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == sys.maxsize:
                print("{:>7s}".format("INF"), end="")
            else:
                print("{:>7d}".format(dist[i][j]), end="")
        print()

# Algorytm Floyd-Warshall
def floydWarshall(graph):
    # Inicjalizacja macierzy odległości
    dist = [[0 for x in range(V)] for y in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    # Relaksacja krawędzi
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Wyświetlenie rozwiązania
    printSolution(dist)

if __name__ == "__main__":
    # Graf wejściowy
    graph = [[0,   5,  sys.maxsize, 10],
             [sys.maxsize, 0,   3, sys.maxsize],
             [sys.maxsize, sys.maxsize, 0,   1],
             [sys.maxsize, sys.maxsize, sys.maxsize, 0]
             ]
 
    # Wywołanie algorytmu i wyświetlenie rozwiązania
    floydWarshall(graph)
