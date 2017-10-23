def getList(n):
    if n == 2:
        return [2]
    l = getList(n-1)
    for i in l:
        if n % i == 0:
            n /= i
    l.append(n)
    return l

def getMin(n):
    l = getList(n)
    c = 1
    for i in l:
        c *= i
    return c
cProfile.run('getMin(100)')