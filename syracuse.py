def syracuse(n):
    c = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        c += 1
    return c


def getMaxSyracuse(n):
    c = 0
    mx = n
    for i in xrange(1, n + 1):
        s = syracuse(i)
        if c < s:
            c = s
            mx = i
    return mx, c


d = {0: 0, 1: 0}


def syracuse2(n):
    global d
    if n in d:
        return d[n]
    v = syracuse2(n / 2) + 1 if n % 2 == 0 else syracuse2(3 * n + 1) + 1
    d[n] = v
    return v


def getMax(n):
    for i in xrange(1, n + 1):
        syracuse2(i)
    k = max(d, key=d.get)
    return k, d[k]


result = map(syracuse2, range(1000000))
print max(result)
print result.index(max(result))

from numba import jit


@jit
def syracuse(n):
    c = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        c += 1
    return c


@jit
def getMaxSyracuse(n):
    c = 0
    mx = n
    for i in xrange(1, n + 1):
        s = syracuse(i)
        if c < s:
            c = s
            mx = i
    return mx, c