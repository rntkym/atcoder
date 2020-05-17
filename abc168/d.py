n, m = map(int, input().split())
edge_list = [[] for i in range(n)]
prev_list = [1]
ans = [0] * n

for i in range(m):
    a, b =  map(int, input().split())
    edge_list[a - 1].append(b)
    edge_list[b - 1].append(a)

while len(prev_list) > 0:
    next = []
    for prev in prev_list:
        for edge in edge_list[prev - 1]:
            if ans[edge - 1] == 0:
                next.append(edge)
                ans[edge - 1] = prev
    prev_list = next

print('Yes')
for i in range(1, len(ans)):
    print(ans[i])
