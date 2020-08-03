n = int(input())
c_list = list(input())
start = 0
end = n
ans = 0

while 1:
    for i in range(start, n):
        start = i
        if c_list[i] == "W":
            break
    for i in reversed(range(end)):
        end = i
        if c_list[i] == "R":
            break
    if start >= end:
        break

    c_list[start], c_list[end] = c_list[end], c_list[start]
    start += 1
    ans += 1

print(ans)
