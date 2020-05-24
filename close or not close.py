number1= float(input("Please enter first floating point number: "))
number2= float(input("Please enter second floating point number: "))

if abs(number2-number1) <= 0.001 and abs(number1-number2)<=0.001:
    print("Close")
else:
    print("Not close")
    
