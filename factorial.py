def factorial(n):
   fact = 1
   try:
      for i in range(1,n+1):
         fact = fact * i
   except:
      print("wrong input")
   print (fact)

factorial(5)
