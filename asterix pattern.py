a = int(input("Please input the number of stars in the pattern: "))
for i in range (a):
    for j in range(i):
        print("*",end="")
    print("")

for i in range (a,-1,-1):
    for j in range(i):
        print("*",end="")
    print("")

for i in range(a):
    print("*"*i,end="\n")
for i in range(a,-1,-1):
    print("*"*i,end="\n")
