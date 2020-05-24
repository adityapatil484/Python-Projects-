formula = input("Please enter the formula: ")
formula = list(formula)
Open = 0
Close = 0
for character in formula:
    if character == "(":
        Open = Open + 1
    elif character  == ")":
        Close = Close + 1

if Open == Close:
    print("The formula is valid")
else:
    print("The formula is invalid")

        
