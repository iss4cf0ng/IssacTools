xlst = [n**2 for n in range(0, 10)]
print(xlst)

maxiumn = eval(input("Maximum : "))
x = [[a, b, c] for a in range(1, maxiumn) for b in range(1, maxiumn) for c in range(1, maxiumn) if a**2 + b**2 == c**2]
print(x)