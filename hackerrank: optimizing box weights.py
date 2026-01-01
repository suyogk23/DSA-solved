#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimalHeaviestSetA(arr):
    # Write your code here
    n = len(arr)
    #sort arr: n log n
    arr.sort()
    # prefix sum 
    prefixSum = sum(arr)
    # trasverse from last
    subSetA = []
    sumSubSetA = 0
    for i in range(n-1, -1, -1):
        if sumSubSetA <= prefixSum:
            prefixSum -= arr[i]
            sumSubSetA += arr[i]
            subSetA = [arr[i]] + subSetA
        else:
            break
    return subSetA
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = minimalHeaviestSetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

