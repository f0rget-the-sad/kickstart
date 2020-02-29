from code import sol

def tests():
    assert sol("2 3 1 2 1 2 1 1 9") == 52
    assert sol("10 10 10001 10002 10003 10004 10005 10006 89273") == 739786670

tests()
print("PASS!")
