import sys

testcases = int(input())

for i in range(testcases):
    a, b = [int(i) for i in input().split()]
    a += 1
    stry = input() # ???
    while(1):
        g = (a+b)//2
        print(g)
        sys.stdout.flush()
        res = input()
        if res == "CORRECT":
            break
        elif res == "TOO_SMALL":
            a = g + 1
        else:
            b = g - 1
