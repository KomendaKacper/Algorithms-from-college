def bfs(G, s):
    queue = [(s, -1)]
    No = []
    i = 1
    No.append((s, i))
    cyclic = False

    while queue:
        s, parent = queue.pop(0)

        for v in G[s]:
            if v not in [node[0] for node in No]:
                i += 1
                queue.append((v,s))
                No.append((v,i))
            elif parent != v:
                cyclic = True

    consistent = True
    if len(No) < len(G.keys()):
        consistent = False
    return No, consistent, cyclic


graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['B', 'C', 'D', 'F'],
    'F': ['E', 'G', 'H', 'I'],
    'G': ['F', 'H', 'I', 'J'],
    'H': ['F', 'G', 'I', 'J'],
    'I': ['F', 'G', 'H', 'J'],
    'J': ['G', 'H', 'I']
}

graph2 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E', 'F'],
    'D': ['A', 'B', 'C', 'E', 'I'],
    'E': ['B', 'C', 'D', 'F', 'G'],
    'F': ['C', 'E', 'G', 'H', 'I'],
    'G': ['E', 'F', 'H', 'I'],
    'H': ['F', 'G', 'I'],
    'I': ['D', 'F', 'G', 'H'],
    'J': []
}

graph3 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A'],
    'D': ['A', 'G', 'H'],
    'E': ['B'],
    'F': ['B'],
    'G': ['D'],
    'H': ['D', 'I', 'J'],
    'I': ['H'],
    'J': ['H']
}

kolejnosc1, consistent1, cyclic1 = bfs(graph1, "A")
kolejnosc2, consistent2, cyclic2 = bfs(graph2, "A")
kolejnosc3, consistent3, cyclic3 = bfs(graph3, "A")

print ("Graf spójny z cyklami:")
print ("Indeksy wierzchołków i kolejność ich odwiedzania: ", kolejnosc1)
print ("Czy spójny: ", consistent1)
print ("Czy ma cykl: ", cyclic1, "\n")

print ("Graf niespójny z cyklami: ")
print ("Indeksy wierzchołków i kolejność ich odwiedzania: ", kolejnosc2)
print ("Czy spójny: ", consistent2)
print ("Czy ma cykl: ", cyclic2, "\n")

print ("Graf spójny acykliczny")
print ("Indeksy wierzchołków i kolejność ich odwiedzania: ", kolejnosc3)
print ("Czy spójny: ", consistent3)
print ("Czy ma cykl: ", cyclic3)