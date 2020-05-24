""" Divisor calculator"""

integer=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,integer+1):
    if(integer%i==0):
        print(i)
