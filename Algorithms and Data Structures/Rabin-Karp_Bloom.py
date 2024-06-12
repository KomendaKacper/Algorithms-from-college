import math
import time

with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()
S = ' '.join(text).lower()

patterns = [
    'gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits',
    'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present',
    'deliver', 'welcome', 'baggins', 'further'
]
P = 0.001
n = len(patterns)
b = int(-(n * math.log(P)) / (math.log(2) ** 2))
k = int((b / n) * math.log(2))

bloom_filter = [False] * b

def hash1(pattern, b):
    return sum(ord(char) for char in pattern) % b

def hash2(pattern, b):
    return sum((i + 1) * ord(char) for i, char in enumerate(pattern)) % b

def add_to_bloom(pattern, bloom_filter, b, k):
    for i in range(k):
        if i % 2 == 0:
            digest = hash1(pattern, b)
        else:
            digest = hash2(pattern, b)
        bloom_filter[digest] = True

for pattern in patterns:
    add_to_bloom(pattern, bloom_filter, b, k)

def might_be_in_bloom(substring, bloom_filter, b, k):
    for i in range(k):
        if i % 2 == 0:
            digest = hash1(substring, b)
        else:
            digest = hash2(substring, b)
        if not bloom_filter[digest]:
            return False
    return True

def RabinKarpBloom(S, patterns, d=256, q=101):
    M = len(S)
    N = len(patterns[0])
    h = 1
    compare_count = 0
    collisions = 0
    matches = {pattern: 0 for pattern in patterns}
    m = 0
    h = pow(d, N-1, q)
    hS = 0
    for i in range(N):
        hS = (d * hS + ord(S[i])) % q
    
    while m <= M - N:
        substring = S[m:m+N]
        compare_count += 1
        if might_be_in_bloom(substring, bloom_filter, b, k):
            for pattern in patterns:
                hW = 0
                for i in range(N):
                    hW = (d * hW + ord(pattern[i])) % q
                if hW == hS and substring == pattern:
                    matches[pattern] += 1
                    break
                else:
                    collisions += 1
        
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
        m += 1
    
    return matches, compare_count, collisions

t_start = time.perf_counter()
bloom_matches, bloom_comparisons, bloom_collisions = RabinKarpBloom(S, patterns)
t_stop = time.perf_counter()
bloom_time = t_stop - t_start

print(f'Filtr Blooma: {sum(bloom_matches.values())};{bloom_comparisons};{bloom_collisions};{bloom_time:.7f}')
