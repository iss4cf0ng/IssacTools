def count_zero(n):
    count = 0
    max_count = 0
    while n > 0:
        r = n % 10
        d = n // 10
        # if n is end with 0 , then n % 10 = 0
        if r == 0:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 0
        n = d # Or n = n // 10
    return max_count

print(count_zero(eval(input('Number: '))))