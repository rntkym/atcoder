import itertools

s =  list(input())
s = [int(i) for i in s]
use_list = []
flag = False

for i in range(9):
    count = s.count(i + 1)
    if count > 0:
        use_list.append(i + 1)
    if count > 1:
        use_list.append(i + 1)
    if count > 2:
        use_list.append(i + 1)

if len(use_list) == 2:
    comb = [[0, s[0], s[1]], [0, s[1], s[0]]]
elif len(use_list) == 1:
    comb = [[0, 0, s[0]]]
else:
    comb = list(itertools.permutations(use_list, 3))

for c in comb:
    num = 100 * c[0] + 10 * c[1] + c[2]
    if num % 8 == 0:
        print("Yes")
        flag = True
        break

if not flag:
    print("No")