str1 = 'hello'
def palindrome(str1):
   if (str1 == str1[::-1]):
      return True
   else:
      return False

print(palindrome('hello'))
