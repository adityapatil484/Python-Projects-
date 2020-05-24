class Password_manager:

   def __init__(self,password):
      self.password = []

   def show_passwords(self):
      for i in range(len(self.password)):
         print(self.password[i])
      
   def get_password(self):
      return self.password[len(self.password)-1]

   def set_password(self):
      if string not in self.password:
         self.password.append(p)
         return 1
      else:
         return  0

   def is_correct(self,string):
      if self.password[len(self.password)-1] == string:
         return True
      else:
         return False


p = ['123','456','789']
p1 = Password_manager(p)
p1.show_passwords()
print("Current Passwords is",p1.get_password())
p1.set_password('hello')
print("Current Password is",p1.get_password())



      
