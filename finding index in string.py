str1 = input("Enter a string: ")
letter = input("Enter a letter: ")
x= len(str1)
i=0
found = False
while(i<x):
    if letter == str1[i]:
        print("Index is: ",i)
        found= True
        break
    i= i+1
if found == False:
    print("Letter is not in string")
