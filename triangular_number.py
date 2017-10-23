from numpy import sqrt

def triangular(n):
    c = 0
    for i in range(n):
        c += i + 1
    return c

def divisor(n):
    i = 1
    if int(sqrt(n))**2 == n:
        d = 1
        while i < sqrt(n):
            if n % i == 0:
                d += 2
            i += 1
        return d
    d = 0
    while i < sqrt(n):
        if n % i == 0:
            d += 2
        i += 1
    return d

def foo(n):
    i = n
    while divisor(triangular(i)) < n:
        i += 1
    return i

print foo(500)