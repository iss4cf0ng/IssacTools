from math import log10, floor

def palindrome(n):
    digits = floor(log10(n)) + 1
    d = digits // 2
    for _ in range(d):
        low = n % 10
        high = n // (10 ** (digits - 1))
        if low != high:
            return False
        n = n % (10 ** (digits-1))
        n = n // 10
        digits -= 2
    return True

n = eval(input('Number : '))
print(palindrome(n))