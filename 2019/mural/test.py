from code import sol

def tests():
    assert sol(4, "1332") == 6
    assert sol(4, "9583") == 14
    assert sol(3, "616") == 7
    assert sol(10, "1029384756") == 31

tests()
print("PASS!")
