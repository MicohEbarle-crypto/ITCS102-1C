for m in range(1, 6 + 1):
    for i in range(6, m, -1):
        print(" ", end=" ")
    for c in range(m, 0, -1):
        print(c, end=" ")
    for o in range(2, m + 1):
        print(o, end=" ")

    print()
    
