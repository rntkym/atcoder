import math

x = int(input())
money = 100
year = 0

while money < x:
    money *= 1.01
    money = math.floor(money)
    year += 1

print(year)
