n, k = map(int, input().split())
a_list = list(map(int, input().split()))

for i in range(n - k):
    if a_list[i] < a_list[i + k]:
        print("Yes")
    else:
        print("No")
