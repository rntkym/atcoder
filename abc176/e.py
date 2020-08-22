h, w, m =  map(int, input().split())
bom_list = []
h_list = [0] * h
w_list = [0] * w

for i in range(m):
    a, b =  map(int, input().split())
    bom_list.append([a - 1, b - 1])
    h_list[a - 1] += 1
    w_list[b - 1] += 1

max_h = max(h_list)
max_w = max(w_list)
ans = max_h + max_w
count = 0

for bom in bom_list:
    if h_list[bom[0]] == max_h and w_list[bom[1]] == max_w:
        count += 1

if h_list.count(max_h) * w_list.count(max_w) == count:
    ans -= 1

print(ans)
