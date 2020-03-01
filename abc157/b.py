bingo = []
for i in range(3):
    a, b, c = map(int, input().split())
    bingo += [a, b, c]

b_list = []
for i in range(int(input())):
    b_list.append(int(input()))

for i in range(len(bingo)):
    if bingo[i] in b_list:
        bingo[i] = 'X'

pattern_list =[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
flag = 0
for i in range(len(pattern_list)):
    if bingo[pattern_list[i][0]] == 'X' and bingo[pattern_list[i][1]] == 'X' and bingo[pattern_list[i][2]] == 'X':
        flag = 1
        break

if flag == 1:
    print('Yes')
else:
    print('No')
