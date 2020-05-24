class Investment:

   def __init__(self,p,i,):
      self.principal = p
      self.interest = i/100
   

   def value_after(self,n):
      self.period = n
      self.value = self.principal * (1+self.interest)**n
      return self.value

   def __str__(self):
      return "Principal is {} and  Interest is {}".format(self.principal,self.interest)


I1 = Investment(1000,5.12)

print("Value =",I1.value_after(1))

print(I1)

                               
