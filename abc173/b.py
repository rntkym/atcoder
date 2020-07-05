n = int(input())
s_list = []
ans_list = [0, 0, 0, 0]

for i in range(n):
    s_list.append(input())

for i in range(n):
    if s_list[i] == "AC":
        ans_list[0] += 1
    elif s_list[i] == "WA":
        ans_list[1] += 1
    elif s_list[i] == "TLE":
        ans_list[2] += 1
    else:
        ans_list[3] += 1

print("AC x " + str(ans_list[0]))
print("WA x " + str(ans_list[1]))
print("TLE x " + str(ans_list[2]))
print("RE x " + str(ans_list[3]))
