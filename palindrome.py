def foo():
    n = 100
    m = 100
    p = 0
    while n < 1000:
        while m < 1000:
            if n * m > p and isPalindrom(n * m):
                p = n * m
                p1 = n
            m += 1
        m = 100
        n += 1
    return p, p1, p / p1


def isPalindrom(n):
    n = list(str(n))
    if n == n[::-1]:
        return True
    return False


import cProfile

cProfile.run("foo()")