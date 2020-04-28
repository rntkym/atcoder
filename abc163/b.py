n, m = map(int, input().split())
hw_list = list(map(int, input().split()))
sum = 0

for i in range(m):
    sum += hw_list[i]

if sum > n:
    print(-1)
else:
    print(n - sum)
