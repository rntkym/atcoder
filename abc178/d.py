import math
from scipy.special import comb

s = int(input())
m = 10 ** 9 + 7

if s < 3:
    print(0)
else:
    element = math.floor(s / 3)
    ans = 0
    for i in range(1, element + 1):
        n = (s - 3 * i) + (i - 1)
        r = i - 1
        c = comb(n, r, exact=True)
        ans += c
    print(ans % m)
