alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]

print(alist[0](10), alist[1](2, 20), alist[2](3))

key = 'm'

aDict = {'m': lambda x:2*x, 'n': lambda x:3*x}

print(aDict[key](9)) # Output: 18
### comment line