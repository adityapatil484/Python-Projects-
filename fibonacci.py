def fibonacci(n):
   x = 0
   y = 1
   print(x)
   print(y)
   for i in range(n-2):
      print(x+y)
      temp = y
      y = x + y
      x = temp

fibonacci(10)
