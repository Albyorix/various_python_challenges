def st(s):
    s = s.split()
    l = []
    for i in s:
        l.append(int(i))
    l.sort()
    if l[1] - l[0] > l[-1] - l[-2]:
        return (l[0] + l[1]) / 2
    s = []
    for i in range(len(l)):
        s.append((l[1] - l[0]) * i - l[i] + l[0])
    for i in range(len(s)):
        if s[i] < 0:
            return (l[i] + l[i - 1]) / 2


from random import shuffle, seed

seed(1)  # Nessecary because of the randomness the result can change a lot
t = range(0, 10000000, 3)
shuffle(t)
a = t.pop()
s = ''
for i in t:
    s += " " + str(i)


def tt():
    return st(s)


print tt(), a