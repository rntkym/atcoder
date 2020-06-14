x, n = map(int, input().split())
if n == 0:
    print(x)
    exit()

p_list = list(map(int, input().split()))
counter = 1

if x in p_list:
    while 1:
        if (x - counter) not in p_list:
            print(x - counter)
            break
        elif (x + counter) not in p_list:
            print(x + counter)
            break
        counter += 1
else:
    print(x)
