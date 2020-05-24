"""computes greatest common divisor"""

x =int(input("Enter an integer: "))
y =int(input("Enter another integer: "))
if (x>y):
    large=x
    small=y
else:
    large=y
    small=x

while(small!=0):
     temp=small
     small = large%small
     large=temp

print("GCD = ",large)

