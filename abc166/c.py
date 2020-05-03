n, m = map(int, input().split())
h_list = list(map(int, input().split()))
n_list = [''] * n
ans = 0

for i in range(m):
    a, b = map(int, input().split())
    if h_list[b - 1] >= h_list[a - 1]:
        n_list[a - 1] = 'x'
    if h_list[a - 1] >= h_list[b - 1]:
        n_list[b - 1] = 'x'

for i in range(n):
    if n_list[i] == '':
        ans += 1

print(ans)
