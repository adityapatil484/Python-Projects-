def fact(n):
    if (n == 0):
        return 1
    ret = n*fact(n-1)
    return ret

print (fact(993))
