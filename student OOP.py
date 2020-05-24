class Student:

   def __init__(self,name,telephone,age):
      self.name = name
      self.telephone = telephone
      self.age = age

   def __len__(self):
      return (len(self.name))

   def __str__(self):
      return """Name of student : {}
                Telephone of student : {}
                Age of student : {}""".format(self.name,self.telephone,self.age)

s1 = Student('Tom','999-999-999',25)

print(s1)

l_name = len(s1)

print("Length of name is: ",l_name)

s2 = s1

print(s2)


s2.name = 'Harry'

print("-"*10)

print(s1)

print(s2)
