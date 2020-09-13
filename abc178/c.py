n = int(input())
m = 10 ** 9 + 7

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    ans = (10 ** n - 9 ** n * 2 + 8 ** n) % m
    print(ans)
