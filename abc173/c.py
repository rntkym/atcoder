import itertools
import copy

h, w, k =  map(int, input().split())
c_list = []
ans = 0
for i in range(h):
    c = list(input())
    c_list.append(c)

p_list = list(itertools.product(range(0, 2), repeat = (h + w)))

for i in range(len(p_list)):
    damy = copy.deepcopy(c_list)
    for j in range(h):
        if p_list[i][j] == 1:
            damy[j] = ["."] * w
    for j in range(w):
        if p_list[i][h + j] == 1:
            for l in range(h):
                damy[l][j] = "."
    count = 0
    for j in range(h):
        count += damy[j].count('#')
    if count == k:
        ans += 1

print(ans)
