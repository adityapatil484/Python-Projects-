i=0
while True:
    print('i = ',i)
    i = i+1
    j=0
    while True:
        print('j = ',j)
        j = j+1
        if (j==3):
            print("breaking inner while loop")
            
    if (i==5):
        print("breaking outer while loop")
        break
