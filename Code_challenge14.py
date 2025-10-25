anime_list = [ ]

micoh= True
while micoh == True:
    anlist = input("Enter an anime (or type \"exit\" to stop): ")

    if anlist == "Exit":
        print("You are exited to the anime ----> ")
        break
    else:
        animelist.append(anlist)
        continue
print("Here is the list of animes ---> ")
for a in animelist:
    print(f"-{a}")
