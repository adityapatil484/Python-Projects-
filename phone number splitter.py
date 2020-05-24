number = input("Please enter a phone number: ")


parts = number.split("-")

print("Country code is", parts[0])
print("State code is", parts[1])
print("phone number is",parts[2])

