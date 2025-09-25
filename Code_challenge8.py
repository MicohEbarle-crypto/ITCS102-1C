print("Multiplication Maker")
print("--------------------------")
M = eval(input("Give me number to create a multiplication table: "))
for i in range(1,11,1):
    print(M, "x", i, "=", M*i)
