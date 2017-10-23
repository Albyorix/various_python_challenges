from numpy import sqrt

def listPrime(n):
    l = [2]
    for i in range(3, n, 2):
        if isPrime(i):
            l.append(i)
    return l

def isPrime(n):
    i = 3
    while i < sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True

print sum(listPrime(20000))