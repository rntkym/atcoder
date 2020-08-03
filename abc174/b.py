import math

n, d =  map(int, input().split())
ans = 0
for n in range(n):
    x, y = map(int, input().split())
    if math.sqrt(x * x + y * y) <= d:
        ans += 1
print(ans)
