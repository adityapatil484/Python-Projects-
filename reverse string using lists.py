str1=input("Please enter a string: ")

a = len(str1)
reverse = []
for i in range (a-1,-1,-1):
    reverse.append(str1[i])

str2 = ''.join(reverse)
print(str2)
