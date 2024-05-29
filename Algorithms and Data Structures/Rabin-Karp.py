import time
with open("lotr.txt", encoding='utf-8') as f:
    text = f.readlines()
S = ' '.join(text).lower()

def naive(S, W):
    m = 0
    i = 0
    repeats = 0
    compare_count = 0
    
    while m != len(S):
        if S[m] == W[i]:
            if i == (len(W)-1):
                repeats += 1
                i = 0
            else:
                i += 1
            m += 1
        else:
            i = 0
            m += 1
        compare_count += 1
    return repeats, compare_count

def RabinKarp(S, W):
    M = len(S)
    N = len(W)
    hW = hash(W)
    d = 256
    q = 101
    h = 1

    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q
    
    for m in range (M-N+1):
        # hS = hash(S[m:m+N])
        hS = (d * (hash(S[m:m+N]) - ord(S[m]) * h) + ord(S[m + N-1])) % q
        if hS == hW:
            if S[m:m+N] == W:
                return m
    return None

def hash(word, d=256, q = 101):
    hw = 0
    N = len(word)
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

W = "time."

repeats, compare_count = naive(S, W)
print (f'repeats',repeats)
print (f'compares', compare_count)

t_start = time.perf_counter()
naive(S, W)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

m = RabinKarp(S, W)
print (f'm', m)

t_start = time.perf_counter()
RabinKarp(S,W)
t_stop = time.perf_counter()
print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
