def factorial(n):
    print("factorial has been called with n =" +str(n))
    if n==0:
        return 1
    else:
        res = n*factorial(n-1)
        print("intermediate result for ", n, " * factorial(", n-1, "):",res)
        return res

print("final result : ",factorial(7))
