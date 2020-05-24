str1 = 'Hello'
list1 = [1,14,5,9,12]
list2 = ['one','two','three','four','five','six']

list3 = [0 for i in range (10)]
list4 = [i**2 for i in range(1,8)]
list5 = [i*10 for i in list1]
list6 = [c*2 for c in str1]
list7 = [m[0] for m in list2]
list8 = [i for i in list1 if i<10]
list9 = [m[0] for m in list2 if len(m)==3]

print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)

