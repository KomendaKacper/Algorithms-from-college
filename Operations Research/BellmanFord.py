from math import inf

class Graph:
    def __init__(self, vertices):
        self.V = vertices   # Liczba wierzchołków w grafie
        self.graph = []     # Lista krawędzi wraz z ich wagami

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w]) #Dodajemy krawędź wraz z jej wagą

    def bellman_ford(self, src):
        dist = [inf] * self.V  # Dystans każdego wierzchołka początkowo równy nieskończoność
        dist[src] = 0  # Odległość początkowego wierzchołka od niego samego równa 0
        prev = [None] * self.V  # Lista poprzednich wierzchołków na najkrótszych ścieżkach
        prev[src] = src  # Poprzedni wierzchołek dla początkowego to on sam

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != inf and dist[s] + w < dist[d]: #Jeśli dystans aktualnego wierzchołka nie jest równy nieskończoność i dojdziemy krócej do następnego niż poprzednio
                    dist[d] = dist[s] + w
                    prev[d] = s  # Aktualizacja poprzedniego wierzchołka

        #Graf wszystkie wierzchołki mają już swoją najkrótszą trasę. Teraz jeśli znajdziemy jeszcze krótszą, oznaczać to będzie, że występuje ujemny cykl
        for s, d, w in self.graph:
            if dist[s] != inf and dist[s] + w < dist[d]: #Jeśli dystans obecnego nie jest równy nieskończoność i po przejściu dystans jest mniejszy niż poprzednio
                print("Graf ma ujemny cykl!")
                return

        self.print_shortest_paths(src, dist, prev)

    def print_shortest_paths(self, src, dist, prev):
        print("Najkrótsza droga do każdego wierzchołka:")
        for i in range(self.V): 
            path = []
            current = i
            while current != src: #Póki nie dojdziemy do początku grafu
                path.append(current) #Dodajemy do ścieżki wierzchołek
                current = prev[current] #Przechodzimy do wierzchołka przed poprzednikiem 
            path.append(src) 
            path.reverse()
            print(f'Ścieżka do wierzchołka {i}: {path}, koszt: {dist[i]}')

g = Graph(11)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(0, 5, 4)
g.add_edge(1, 4, 3)
g.add_edge(1, 3, 1)
g.add_edge(1, 2, 4)
g.add_edge(2, 3, 2)
g.add_edge(2, 6, 4)
g.add_edge(3, 4, 3)
g.add_edge(4, 5, 2)
g.add_edge(4, 7, 1)
g.add_edge(5, 7, 4)
g.add_edge(5, 6, 2)
g.add_edge(5, 8, 3)
g.add_edge(7, 8, 4)
g.add_edge(8, 9, 4)
g.add_edge(8, 10, 5)
g.add_edge(9, 10, 4)
g.bellman_ford(0)
