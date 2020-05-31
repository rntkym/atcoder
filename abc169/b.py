n = int(input())
a_list = list(map(int, input().split()))
ans = 1

if 0 in a_list:
    print(0)
    exit()

for i in range(n):
    ans *= a_list[i]
    if len(str(ans)) > 19 or ans > 10 ** 18:
        print(-1)
        exit()

print(ans)
