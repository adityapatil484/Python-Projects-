d = [{'name':'Todd', 'phone':'555-1414','email':'todd@mail.net'},{'name':'Helga', 'phone':'555-1618','email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141','email':''},{'name':'LJ', 'phone':'555-2718','email':'lj@mail.net'}]


print("Users whose number ends with 8: ")
for i in range(len(d)):
    if d[i]['phone'][-1] == '8':
        print(d[i]['name'])

        
print("Users who dont have an email:")
for i in range(len(d)):
    if d[i]['email'] =='':
        print(d[i]['name'])
            
