def foo():
    for a in range(1, 499):
        for b in range(a, 499):
            if a * a + b * b == (1000 - a - b) ** 2:
                return a, b


print foo()