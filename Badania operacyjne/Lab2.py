# def bfs (graph, node):
#     queue = [node]
#     visited = [node]

#     while queue:
#         s = queue.pop(0)
#         print (s)

#         for x in graph[s]:
#             if x not in visited:
#                 queue.append(x)
#                 visited.append(x)

def dfs (G, s):
    i = 1
    visited = []
    stack = []

    visited.append((s,i))
    stack.append(s)

    while stack:
        s = stack.pop()
        print (s)

        for v in reversed(G[s]):
            k = 0
            for e in visited:
                if v in e[0]:
                    k += 1
            if k == 0:
                i += 1
                visited.append((v, i))
                stack.append(v)
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['A', 'D'],
    'D': ['A']
}

print (dfs(graph , "A"))