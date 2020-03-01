n, m = map(int, input().split())
num_list = ['X'] * n

def ans():
    if n == 1 and m == 0:
        return 0
    for i in range(m):
        set = list(map(str, input().split()))
        if set[0] == '1' and set[1] == '0' and n != 1:
            return -1
        else:
            if num_list[int(set[0]) - 1] == 'X':
                num_list[int(set[0]) - 1] = set[1]
            elif num_list[int(set[0]) - 1] == set[1]:
                continue
            else:
                return -1

    for i in range(n):
        if num_list[i] == 'X':
            num_list[i] = '1' if i == 0 else '0'

    return ''.join(num_list)

print(ans())
