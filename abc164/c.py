n = int(input())
s_list = []

for i in range(n):
    s_list.append(input())

print(len(list(set(s_list))))
