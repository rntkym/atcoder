import sys

n = int(input())
a_list = list(map(int, input().split()))
trade_list = []
prev = "+"
money = 1000
stok = 0

while a_list[len(a_list) - 1] <= a_list[len(a_list) - 2]:
    a_list.pop()
    if len(a_list) == 1:
        print(1000)
        sys.exit()

while a_list[0] >= a_list[1]:
    a_list.pop(0)
    if len(a_list) == 1:
        print(1000)
        sys.exit()

trade_list.append(a_list[0])

for i in range(len(a_list) - 1):
    if a_list[i] > a_list[i + 1]:
        now = "-"
    elif a_list[i] < a_list[i + 1]:
        now = "+"
    else:
        now = prev

    if prev != now:
        trade_list.append(a_list[i])
    prev = now

trade_list.append(a_list[-1])

for i in range(len(trade_list)):
    if i % 2 == 0:
        stok = money // trade_list[i]
        money -= stok * trade_list[i]
    else:
        money += stok * trade_list[i]

print(money)
