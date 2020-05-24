str1= "HELLO"


print("Length of string", len(str1))

print(str1 * 10)

print(str1[0])

print(str1[:3])

print(str1[-1:-3])

print(str1[-1:])

if len(str1)>= 7:
   print(str1[6])
else:
   print("The string is not long enough")

print(str1[1:-2])

print(str1.lower())


if 'e' in str1:
   str1.replace('e','a')
   print(str1)

