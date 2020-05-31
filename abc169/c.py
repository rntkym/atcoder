import math

a, b = map(str, input().split())
a = int(a)
b = int(b.replace('.', ''))
print(b)
ans = str(a * b)

if len(ans) > 2:
    print(int(ans[:-2]))
else:
    print(0)
