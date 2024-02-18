#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    lst=[0]*n
    for operation in queries:
        for val in operation[:-1]:
            lst[val-1]+=operation[-1]
        for i in range(operation[-2]):
            if lst[i]==0 or (i>operation[0]-1 and i<operation[1]-1):
                lst[i]=operation[-1]
        
    return max(lst)
            


nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(result)
