def converterCurrency(m):
   conversion = m/70
   return conversion

def main():
   m = int(input("Enter the amount of money to be converted: "))
   print(converterCurrency(m))

if __name__ == "__main__":
   main()
