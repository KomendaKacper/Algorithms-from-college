#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinimumOperations(arr):
    l = 0
    r = len(arr)-1
    res = 0
    
    while l < r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            if arr[l] < arr[r]:
                arr[l+1] = arr[l] + arr[l+1]
                arr = arr[:l] + arr[l+1:]
                r -= 1
                res += 1

            if arr[l] > arr[r]:
                arr[r-1] = arr[r] + arr[r-1]
                arr = arr[:r] + arr[r+1:]
                r -= 1
                res += 1
                
        print (arr)
    return res

tab = [10,10,63,12,39,77,9,63,12,39,10]
print (getMinimumOperations(tab))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = []

#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)

#     result = getMinimumOperations(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
