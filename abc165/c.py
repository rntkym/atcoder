import itertools

n, m, q = map(int, input().split())
abcd = []
ans = 0

for i in range(q):
    abcd .append(list(map(int, input().split())))

for comb in list(itertools.combinations_with_replacement(range(1, m + 1),n)):
    sum = 0
    for i in range(q):
        if comb[abcd[i][1] - 1] - comb[abcd[i][0] - 1] == abcd[i][2]:
            sum += abcd[i][3]
    if ans < sum:
        ans = sum

print(ans)
