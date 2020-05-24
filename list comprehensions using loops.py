list1 = [1,14,5,9,12]

list2 = ['One','Two','Three','Four','Five','Six']

list3 = []

list4 =[]

for i in list1:
    if i<10:
        list3.append(i)


for i in list2:
    if len(i) == 3:
        list4.append(i[0])

print(list3,list4)
            
    
list4 = [[i,j] for i in  range(2) for j in range(3)]
print(list4)
