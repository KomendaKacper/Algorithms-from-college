def delete(s):
    l = len(s)
    i = 0
    while i != len(s):
        if s[i] == "A" and s[i+1] == "B" or s[i] == "C" and s[i+1] == "D":
            s = s[:i] + s[i+2:]    
            i -= 1
        else:
            i += 1
        if i < 0:
            i = 0
    return s

s = "CABDCDADBACDB"
print (delete(s))