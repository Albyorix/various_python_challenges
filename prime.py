from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def p3(n):
    c = 0
    for i in range(1,n):
        if isPrime(i):
            c += 1
    return c

def p2(n):
    L = range(2, n+1)
    for i in xrange(2, int(sqrt(n)) + 1):
        if isPrime(i):
            for j in xrange(len(L)-1, L.index(i), -1):
                if L[j] % i == 0:
                    L[j] = 1
    n = 0
    for i in L:
        if i != 1:
            n += 1
    return n

def p(n):
    L = range(2, n+1)
    for i in xrange(2, int(sqrt(n)) + 1):
        try:
            for j in xrange(len(L)-1, L.index(i), -1):
                if L[j] % i == 0:
                    L[j] = 1
        except:
            pass
    n = 0
    for i in L:
        if i != 1:
            n += 1
    return n

import cProfile
n=100000
cProfile.run("p3(n)")
cProfile.run("p2(n)")