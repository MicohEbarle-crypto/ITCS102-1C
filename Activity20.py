isDirty = True  
while isDirty == True:
  wash_again = input("Continue washing the cloths (yes / no)--> ").lower() 
  if wash_again == "yes": 
    print("Washing the clothes again...")
    continue 
  else: 
    print("Washing stops now...")
    break
