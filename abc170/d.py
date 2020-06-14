n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
ans_list = [0] * (a_list[n - 1] + 1)
ans = 0

for a in a_list:
    if ans_list[a] >= 1:
        ans_list[a] += 1
        continue
    for j in range(2 * a, a_list[n - 1] + 1, a):
        ans_list[j] += 1
    ans_list[a] = 1

for a in a_list:
    if ans_list[a] == 1:
        ans += 1
print(ans)
