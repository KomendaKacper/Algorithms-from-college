def GTSP(G):
    visited = []
    Gsorted = sorted(G, key=lambda x: x[2], reverse = True)
    res = []
    i = 0

    while len(res) != G[-1][0]:
        for s in Gsorted:
            if s[1] not in res:
                res.append(s)
    return res

G = [[1,2,3],[1,3,2],[1,4,1],[2,4,3],[2,5,4],[2,6,2],[3,4,5],[3,5,3],[4,5,2]]
print (GTSP(G))