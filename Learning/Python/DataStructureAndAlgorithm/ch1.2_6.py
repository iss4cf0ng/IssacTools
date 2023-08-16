def GCD(m, n):
    if n == 0:
        return m
    return GCD(n, m % n)

a, b = map(int, input('Numbers : ').split())
print(GCD(a, b))