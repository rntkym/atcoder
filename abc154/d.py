n, k = map(int, input().split())
p_list = list(map(int, input().split()))
num = sum(p_list[0:k])
max = 0
index = 0
value = 0

for i in range(n - k):
    num = num + p_list[i + k] - p_list[i]
    if num > max:
        max = num
        index = i + 1

for i in range(k):
    value += (1 + p_list[index + i])/ 2

print(value)
