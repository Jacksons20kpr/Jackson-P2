#Name: Jackson Shangraw
#Date:21/03/24
#Purpose: Sorting and Searching
names =  ["Jackson","Anton","Cameron","Shane","Ethan","Mary","Nate","Reagan","Don","Mark","Wes","Parker","Yuri","Ian","Owen"]
x = sorted(names)
print(x)

f = input("Which name do you want to find?: ")

if f in names: 
    print(names.index(f))
else: 
    print("Name not found")    