n =  int(input())
v_list = []
flag = False

for i in range(n):
    x, y =  map(int, input().split())
    v_list.append([x, y])

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        try:
            ij = (v_list[j][0] - v_list[i][0]) / (v_list[j][1] - v_list[i][1])
        except ZeroDivisionError:
            ij = "Zero"
        for k in range(j + 1, n):
            try:
                ik = (v_list[k][0] - v_list[i][0]) / (v_list[k][1] - v_list[i][1])
            except ZeroDivisionError:
                ik = "Zero"
            if ij == ik:
                print("Yes")
                flag = True
                break
        if flag:
            break
    if flag:
        break

if not flag:
    print("No")