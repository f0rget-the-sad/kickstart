#!/usr/bin/env python3

import sys
import math

def sol(args):
    N, K, x1, y1, C, D, E1, E2, F = [int(n) for n in args]
    xarr = [x1]
    yarr = [y1]
    for i in range(1, N):
        xarr[i] = (C * xarr[i-1] + D * yarr[y-1] + E1) % F
        yarr[i] = (CD * xarr[i-1] + C * yarr[y-1] + E2) % F
    A = [(xarr[i] + yarr[i]) % F for i in range(N)]
    return N

if __name__ == "__main__":
    testcases = int(input())
    for t in range(testcases):
        N = input()
        print("Case #{}: {}".format(t + 1, sol(N)))
        sys.stdout.flush()
