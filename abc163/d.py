n, m = map(int, input().split())
sum = 0

for i in range(m, n + 2):
    min = (i - 1) * i / 2
    max = (2 * n - i + 1) * i / 2
    sum += max - min + 1
print(int(sum % (10 ** 9 + 7)))
