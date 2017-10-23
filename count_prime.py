import numpy as np

def isPrime(n):
    i = 2
    while i <= np.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

n = 10001
l = range(1, n + 1)
l2 = l
cpt = -1
for i in l:
    if isPrime(i):
        cpt += 1
    l2[i-1] = cpt
print l2[-1]