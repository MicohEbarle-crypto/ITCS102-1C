print("\t\t\t\t *", end=' ')
for m in range(1,10,1):
    for i in range(10,m,-1):
        print(' ',end=' ')
    for c in range(1,m,1):
        print('*',end=' ')
    for o in range(1,m,1):
        print('*',end=' ')
    print()
for m in range(10,1,-1):
    for i in range(10,m,-1):
        print(' ',end=' ')
    for c in range(1,m,1):
        print('*',end=' ')
    for o in range(1,m,1):
        print('*',end=' ')
    print()
print("\t\t\t\t *", end=' ')
