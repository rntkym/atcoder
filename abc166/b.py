n, k = map(int, input().split())
sunuke = [0] * n
ans = 0

for i in range(k):
    d = int(input())
    a_list = list(map(int, input().split()))
    for a in a_list:
        sunuke[a - 1] += 1

for s in sunuke:
    if s == 0:
        ans += 1

print(ans)
