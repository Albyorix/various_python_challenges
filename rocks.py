def maximum_piles(n):
    if n <= 2:
        return 1
    cpt = 0
    i = 0
    while cpt <= n:
        i += 1
        cpt += i
    return i - 1


# for n in range(51):
#    print n,maximum_piles(n)


def get_possible_split(n):
    if n == 0:
        return None
    if n <= 2:
        return [n]
    L = []
    for k in range(2, maximum_piles(n) + 1):
        for i in range(1, n / k):
            L = [i] + get_possible_split(n)
    return L


def get_parite(n):
    parite = [0, 0, 0, 1, 0]
    if n <= 4:
        return parite[n]
    for i in range(5, n + 1):
        for k in range(2, maximum_piles(i)):
            pass


print get_possible_split(3)


l = [1]
l2 = [2,3]
l3 = l + l2
print l3