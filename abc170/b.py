x, y = map(int, input().split())

if y > 4 * x or y < 2 * x:
    print('No')
elif (4 * x - y) % 2 == 0:
    print('Yes')
else:
    print('No')
