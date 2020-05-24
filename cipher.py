string = "PYTHON"

cipher = ""

for c in string:
    cipher = cipher + str(ord(c))

print(cipher)
decipher = ""
"""

for i in range(0,len(cipher),2):
    number = int(cipher[i]+cipher[i+1])
    decipher = decipher + chr(number)

print(decipher)
"""          

for i in range (0,len(cipher),2):
    decipher = decipher + chr(int(cipher[i:i+2]))
print(decipher)
