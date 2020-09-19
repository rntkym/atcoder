n = int(input())
divisors_list = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        divisors_list[j] += 1

ans = sum(divisors_list) - divisors_list[-1]
print(ans)
