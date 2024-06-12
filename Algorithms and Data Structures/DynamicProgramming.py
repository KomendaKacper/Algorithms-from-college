def string_compare_recursive(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    substitution_cost = string_compare_recursive(P, T, i-1, j-1) + (P[i] != T[j])
    insertion_cost = string_compare_recursive(P, T, i, j-1) + 1
    deletion_cost = string_compare_recursive(P, T, i-1, j) + 1
    return min(substitution_cost, insertion_cost, deletion_cost)

def string_compare_dp(P, T):
    m, n = len(P), len(T)
    D = [[0] * n for _ in range(m)]
    parents = [['X'] * n for _ in range(m)]

    for i in range(1, m):
        D[i][0] = i
        parents[i][0] = 'D'
    for j in range(1, n):
        D[0][j] = j
        parents[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            cost_substitution = D[i-1][j-1] + (P[i] != T[j])
            cost_insertion = D[i][j-1] + 1
            cost_deletion = D[i-1][j] + 1

            D[i][j] = min(cost_substitution, cost_insertion, cost_deletion)

            if D[i][j] == cost_substitution:
                parents[i][j] = 'S' if P[i] != T[j] else 'M'
            elif D[i][j] == cost_insertion:
                parents[i][j] = 'I'
            else:
                parents[i][j] = 'D'
    return D, parents

def reconstruct_path(parents, start_i, start_j):
    path = []
    i, j = start_i, start_j

    while not (i == 0 and j == 0):
        path.append(parents[i][j])
        if parents[i][j] in ['S', 'M']:
            i -= 1
            j -= 1
        elif parents[i][j] == 'I':
            j -= 1
        else:
            i -= 1
    return ''.join(path[::-1])

def reconstruct_lcs_path(P, parents, start_i, start_j):
    path = []
    i, j = start_i, start_j

    while i > 0 and j > 0:
        if parents[i][j] == 'M':
            path.append(P[i])
            i -= 1
            j -= 1
        elif parents[i][j] == 'I':
            j -= 1
        else:
            i -= 1
    return ''.join(path[::-1])

def string_compare_subsequence(P, T):
    m, n = len(P), len(T)
    D = [[0] * n for _ in range(m)]
    parents = [['X'] * n for _ in range(m)]

    for i in range(1, m):
        D[i][0] = i
        parents[i][0] = 'D'

    for j in range(1, n):
        parents[0][j] = 'X'

    for i in range(1, m):
        for j in range(1, n):
            cost_substitution = D[i-1][j-1] + (P[i] != T[j])
            cost_insertion = D[i][j-1] + 1
            cost_deletion = D[i-1][j] + 1

            D[i][j] = min(cost_substitution, cost_insertion, cost_deletion)

            if D[i][j] == cost_substitution:
                parents[i][j] = 'S' if P[i] != T[j] else 'M'
            elif D[i][j] == cost_insertion:
                parents[i][j] = 'I'
            else:
                parents[i][j] = 'D'

    i, j = m - 1, 0
    for k in range(1, n):
        if D[i][k] < D[i][j]:
            j = k
    return D, parents, i, j

def string_compare_lcs(P, T):
    m, n = len(P), len(T)
    D = [[0] * n for _ in range(m)]
    parents = [['X'] * n for _ in range(m)]

    for i in range(1, m):
        D[i][0] = i
        parents[i][0] = 'D'
    for j in range(1, n):
        D[0][j] = j
        parents[0][j] = 'I'

    for i in range(1, m):
        for j in range(1, n):
            if P[i] == T[j]:
                cost_substitution = D[i-1][j-1]
            else:
                cost_substitution = D[i-1][j-1] + float('inf')
            cost_insertion = D[i][j-1] + 1
            cost_deletion = D[i-1][j] + 1

            D[i][j] = min(cost_substitution, cost_insertion, cost_deletion)

            if D[i][j] == cost_substitution:
                parents[i][j] = 'M' if P[i] == T[j] else 'S'
            elif D[i][j] == cost_insertion:
                parents[i][j] = 'I'
            else:
                parents[i][j] = 'D'
    return D, parents

def longest_common_subsequence(P, T):
    P = ' ' + P
    T = ' ' + T
    D, parents = string_compare_lcs(P, T)
    lcs = []

    i, j = len(P) - 1, len(T) - 1
    while i > 0 and j > 0:
        if parents[i][j] == 'M':
            lcs.append(P[i])
            i -= 1
            j -= 1
        elif parents[i][j] == 'I':
            j -= 1
        else:
            i -= 1

    return ''.join(reversed(lcs))

def longest_monotonic_subsequence(T):
    n = len(T)
    if n == 0:
        return ''
    
    D = [1] * n
    parents = ['X'] * n
    for i in range(1, n):
        for j in range(i):
            if T[i] > T[j] and D[i] < D[j] + 1:
                D[i] = D[j] + 1
                parents[i] = j
    max_len = max(D)
    max_index = D.index(max_len)
    lms = []
    while max_index != 'X':
        lms.append(T[max_index])
        max_index = parents[max_index]
    return ''.join(reversed(lms))[1:]

P = ' kot'
T = ' pies'
cost_recursive = string_compare_recursive(P, T, len(P)-1, len(T)-1)
print("Koszt rekurencji (kot vs pies):", cost_recursive)

P = ' biały autobus'
T = ' czarny autokar'
D, parents = string_compare_dp(P, T)
cost_dp = D[len(P)-1][len(T)-1]
print("Koszt DP (biały autobus vs czarny autokar):", cost_dp)

P = ' thou shalt not'
T = ' you should not'
D, parents = string_compare_dp(P, T)
path = reconstruct_path(parents, len(P)-1, len(T)-1)
print("Zrekonstruowana ścieżka (thou shalt not vs you should not):", path)

P = ' ban'
T = ' mokeyssbanana'
D, parents, start_i, end_j = string_compare_subsequence(P, T)
print("Najlepsze dopasowanie 'ban' zaczyna się na indeksie:", end_j - len(P) + 2)

P = ' bin'
D, parents, start_i, end_j = string_compare_subsequence(P, T)
print("Najlepsze dopasowanie 'bin' zaczyna się na indeksie:", end_j - len(P) + 2)

P = ' democrat'
T = ' republican'
D, parents = string_compare_lcs(P, T)
path = reconstruct_lcs_path(P, parents, len(P)-1, len(T)-1)
print("Najdłuższa wspólna sekwencja (democrat vs republican):", path)

T = ' 243517698'
lms = longest_monotonic_subsequence(T)
print("Najdłuższa monotoniczna podsekwencja (243517698):", lms)

