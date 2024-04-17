#Wyznaczanie zer niezależnych, krok zwiększania liczby zer niezależnych

tab = [[0,1,0,1], [2,0,3,0], [9,5,0,0], [0,0,0,6]]

for e in tab:
    print (e)

def zeros(tab):
    n = len(tab)
    res = [[None]*n]*n 

    for row in tab:
        for col in row:
            
            
    print (res)

print (zeros(tab))