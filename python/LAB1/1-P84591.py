########################################

def absValue(n):
    return n if n >= 0 else -n
    #return abs(n)


########################################

def power(a, b):
    if b == 0: return 1
    aux = power(a, b//2)
    return aux * aux if b % 2 == 0 else aux * aux * a
    #return a**b


########################################

def isPrime(n):
    if n < 2: return False
    for d in range(2, n):
        if n % d == 0: return False
    return True
    #return not len([x for x in range(2,n) if n % x == 0]) > 0


########################################

def slowFib(n):
    if n == 0: return 0
    return 1 if n < 2 else slowFib(n-1) + slowFib(n-2)


########################################

def quickFib(n):
    a = 0
    b = 1
    while n > 0:
        aux = a + b
        a = b
        b = aux
        n -= 1
    return a


