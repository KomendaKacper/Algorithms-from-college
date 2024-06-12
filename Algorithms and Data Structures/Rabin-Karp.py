import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()
S = ' '.join(text).lower()
pattern = "time."

def naive(S, W):
    m = 0
    i = 0
    repeats = []
    compare_count = 0
    
    while m != len(S):
        if S[m] == W[i]:
            if i == (len(W)-1):
                repeats.append(m)
                i = 0
            else:
                i += 1
            m += 1
        else:
            i = 0
            m += 1
        compare_count += 1
    return len(repeats), compare_count

def RabinKarp(S, W, d=256, q=101):
    M = len(S)
    N = len(W)
    hW = 0
    hS = 0
    h = 1
    repeats = []
    compare_count = 0
    collisions = 0
    m = 0
    
    for i in range(N-1):
        h = (h * d) % q
    
    for i in range(N):
        hW = (d * hW + ord(W[i])) % q
        hS = (d * hS + ord(S[i])) % q
    
    while m <= M - N:
        compare_count += 1
        if hW == hS:
            if S[m:m+N] == W:
                repeats.append(m)
            else:
                collisions += 1
        
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
        m += 1
    
    return len(repeats), compare_count, collisions

t_start = time.perf_counter()
naive_matches, naive_comparisons = naive(S, pattern)
t_stop = time.perf_counter()
naive_time = t_stop - t_start

print(f'Metoda naiwna: {naive_matches};{naive_comparisons};{naive_time:.7f}')

t_start = time.perf_counter()
rk_matches, rk_comparisons, rk_collisions = RabinKarp(S, pattern)
t_stop = time.perf_counter()
rk_time = t_stop - t_start

print(f'Metoda Rabina-Karpa: {rk_matches};{rk_comparisons};{rk_collisions};{rk_time:.7f}')
