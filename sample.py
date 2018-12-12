alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]

print(alist[0](10), alist[1](2, 20), alist[2](3))