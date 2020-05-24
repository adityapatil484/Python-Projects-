class Human:
   def __init__(self,name,age,telephone):
      self.name = name
      self.age = age
      self.telephone = telephone

   def get_age(self):
      return self.age

   def get_telephone(self):
      return self.telephone

   def get_name(self):
      return self.name

   def increment_age(self):
      self.age = self.age + 1
      

h1 = Human('Aditya',18,8008072903)

print (h1.get_name(),"age is",h1.get_age())

print (h1.get_name(),"telephone no is",h1.get_telephone())

x = h1.increment_age()

print (h1.get_name(),"age is",h1.get_age())




