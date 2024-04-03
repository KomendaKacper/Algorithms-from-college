def mergesort(array):
    leng = len(array)
    if leng == 1:
        return array

    leftarray = []
    rightarray = []
    i = 0

    while i != leng:
        if i < leng/2:
            leftarray.append(array[i])
        else:
            rightarray.append(array[i])
        i += 1
    
    mergesort(leftarray)
    mergesort(rightarray)

    return merge(leftarray, rightarray)


def merge(leftarray, rightarray):
    res = []
    while leftarray and rightarray:
        if leftarray[0] < rightarray[0]:
            res.append(leftarray.pop(0))
        else:
            res.append(rightarray.pop(0))
    while leftarray:
        res.append(leftarray.pop(0))
    while rightarray:
        res.append(rightarray.pop(0))
    return res 

tab = [100, 42, 216,414,65,88,219,140]

print (mergesort(tab))
