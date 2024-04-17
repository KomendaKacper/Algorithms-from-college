from typing import DefaultDict
from math import inf


def findMinRoute(tsp, start):
    sum = 0 #Łączna waga przejść
    counter = 1 #Służy do indeksowania wierzchołków wrzucanych do route
    j = 0
    i = start - 1
    min = inf
    visitedRouteList = DefaultDict(int) # Słownik odwiedzonych wierzchołków
 
    visitedRouteList[start -1] = 1 #Zaczynamy od wierzchołka o indeksie 0, dodajemy do odwiedzonych
    route = [0] * (len(tsp)+ 1) #Tworzymy pustą listę reprezentującą ścieżkę którą tworzymy
    route[0] = start

    while i < len(tsp) and j < len(tsp[i]): #Przechodzimy po całej macierzy sąsiedztwa
        if counter > len(tsp[i]) - 1:
            break #Upewniamy się że nie wyszliśmy za granice indeksów route

        if j != i and (visitedRouteList[j] == 0): #Jeśli ten wierzchołek jest nieodwiedzony i nie wskazujemy na ten sam wierzchołek
            if tsp[i][j] < min: #Jeśli waga przejścia jest mniejsza niż aktualne minimum
                min = tsp[i][j] #Nowa waga przejścia
                route[counter] = j + 1 #Dodajemy do route te przejście
        j += 1
 
        #Sprawdzamy wszystkie ścieżki z i-tego wierzchołka
        if j == len(tsp[i]): #Jak już przejdziemy po wszystkich ścieżkach z wierzchołka i:
            sum += min #Dodajemy do sumy wagę przejścia o najmniejszej wadze
            min = inf #Resetujemy min
            visitedRouteList[route[counter] - 1] = 1 #Aktualizujemy słownik odwiedzonych wierzchołków
            #Aktualizujemy wskaźniki
            j = 0
            i = route[counter] - 1 # i staje się teraz wierzchołkiem do którego przeszliśmy przed chwilą
            counter += 1 
        
    i = route[counter - 1] - 1 #Ustawiamy i na ostatnio odwiedzony wierzchołek
 
    #Dodajemy pierwszy wierzchołek na koniec ścieżki
    route[-1] = route[0]
    sum += tsp[i][0]

    return sum, route
 
if __name__ == "__main__":
 
    tsp = [
    [-1, 20, 15, 40, 25, -10, 35, 50, 45, 30],
    [10, -1, -35, 25, 30, 45, 40, 55, 50, 35],
    [15, 35, -1, 30, 60, 55, 40, 45, 50, 25],
    [20, 25, -30, -1, 70, 65, 60, 55, 40, 35],
    [25, 30, 35, 45, -1, 80, 75, 70, 55, 50],
    [-30, 45, 55, -65, 75, -1, 60, 40, 35, 25],
    [35, 40, -45, 55, 65, 60, -1, 90, 75, 70],
    [40, 45, 50, 60, -70, 40, 90, -1, 105, 55],
    [45, 50, 55, -40, 55, -35, 75, 105, -1, 95],
    [30, 35, 25, -35, 50, 25, 70, 55, 95, -1]
    ]


    sum, route = findMinRoute(tsp, 1)
    print ("Kolejność odwiedzania wierzchołków:",route)
    print ("Koszt przejścia:",sum)