import math

n = int(input())
x_list = list(map(int, input().split()))
m = 0
u = 0
c_list = []

for i in range(n):
    num = abs(x_list[i])
    m += num
    u += num * num
    c_list.append(num)

print(m)
print(math.sqrt(u))
print(max(c_list))