import math

a, b, c, d = map(int, input().split())
t_hit = math.ceil(c / b)
a_hit = math.ceil(a / d)

if t_hit <= a_hit:
    print("Yes")
else:
    print("No")
