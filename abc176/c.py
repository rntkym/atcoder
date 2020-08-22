n = int(input())
a_list = list(map(int, input().split()))
ans = 0

for i in range(1, n):
    diff = a_list[i - 1] - a_list[i]
    if diff > 0:
        a_list[i] += diff
        ans += diff

print(ans)
