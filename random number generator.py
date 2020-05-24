import random

def randomNum_generator(n):
   return random.randint(10**(n-1),(10**(n)-1))

def main():
   n = int(input("Enter a number: "))
   print(randomNum_generator(n))

if __name__ == "__main__":
   main()
         
