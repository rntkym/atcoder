k = int(input())
m = 0

for i in range(k):
    m = (m * 10 + 7) % k
    if m == 0:
        break
    elif i == k - 1:
        print(-1)
        exit()

print(i + 1)
