#!/usr/bin/env python3

import sys
import math

def sol(N, arr):
    arr = [int(n) for n in arr]
    subarr_len = math.ceil(N/2)
    subsum = sum(arr[:subarr_len])
    maxp = subsum
    for i in range(N//2):
        subsum += arr[i+subarr_len] - arr[i]
        maxp = max(maxp, subsum)
    return maxp

if __name__ == "__main__":
    testcases = int(input())

    for t in range(testcases):
        N = int(input())
        arr = input()
        print("Case #{}: {}".format(t + 1, sol(N, arr)))
        sys.stdout.flush()
