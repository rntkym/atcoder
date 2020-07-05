n = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
a_list.reverse()
index = 1
counter = 0
ans = a_list[0]

for i in range(2, n):
    ans += a_list[index]
    counter += 1
    if counter == 2:
        counter = 0
        index += 1

print(ans)
