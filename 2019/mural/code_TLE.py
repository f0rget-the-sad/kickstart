#!/usr/bin/env python3
import sys
import math

def sol(N, arr):
    arr = [int(n) for n in arr]
    subarr_len = math.ceil(len(arr)/2)
    mm = 0
    print("sub size ", subarr_len)
    for i in range(len(arr)-subarr_len+1):
        mm = max(sum(arr[i:subarr_len+i]), mm)
    return mm

testcases = int(input())

for t in range(testcases):
    N = int(input())
    arr = input()
    print("Case #{}: {}".format(t+1, sol(N, arr)))
    sys.stdout.flush()
