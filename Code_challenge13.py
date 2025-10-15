name = input("hi, what is your name? ")
print("+++++++++")
print("ODD NUMBER SELECTOR, press e to stop the loop") 
print("+++++++++")
x = True 
sum = 0 
odd = " "
while x== True:
  num = eval(input("input a random number "))
  if num %2 == 1: 
    print("odd number detected") 
    sum += num 
    odd += str(num) 
    continue
  elif num == 0: 
    print("loop terminated") 
    break
  else:
    if num %2==0: 
      print("even number") 
    else: 
      print("undeterminate ")
print(f'hi {name}, the sum of all ODD number is {sum}')
