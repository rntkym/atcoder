n = int(input())
s_list = list(str(input()))
r = 0
g = 0
b = 0

for i in range(n):
    if s_list[i] == 'R':
        r += 1
    elif s_list[i] == 'G':
        g += 1
    else:
        b += 1

ans = r * g * b

for d in range(1, n):
    for i in range(n):
        if i + 2 * d >= n:
            break
        if s_list[i] != s_list[i + d] and \
            s_list[i] != s_list[i + 2 * d] and \
            s_list[i + d] != s_list[i + 2 * d]:
            ans -= 1

print(ans)
