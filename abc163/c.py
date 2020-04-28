n = int(input())
a_list = list(map(int, input().split()))
relation_list = [0] * n

for i in range(n - 1):
    relation_list[a_list[i] - 1] += 1

for i in range(n):
    print(relation_list[i])
