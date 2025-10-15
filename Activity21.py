import random
print("number guesting 1 to 10")
print("-------------")
a = random.randint(1,10)
b= 0
c = True
name = input("input your name ")
while c == True:
    num = eval (input("guest the number 1-10----->"))
    if num == a: 
        b+=1
        print("winner")
        break
    else :
        print("incorrect")
        continue
print(f"hi, {name}, your guesting is correct the number of tries is {b}")
