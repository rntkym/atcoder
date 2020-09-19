n, x, m =  map(int, input().split())
ans = 0
loop_list = [0] * m
loop_list[x] = 1
a_list = [x]

for i in range(1, m + 1):
    x = pow(x, 2, m)
    if loop_list[x] != 1:
        loop_list[x] = 1
        a_list.append(x)
    else:
        break

index = a_list.index(x)
time = (n - index) // (len(a_list) - index)
mod = (n - index) % (len(a_list) - index)

ans += sum(a_list[:index])
ans += sum(a_list[index:]) * time
ans += sum(a_list[index:index + mod])

print(ans)
