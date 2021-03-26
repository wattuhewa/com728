#recursive function
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) +fib(n-2)

#iterative solution

def fibi(n):
    old, new = 0, 1
    if n==0:
        return 0
    for i in range (n-1):
        old, new = new, old+new
    return new





