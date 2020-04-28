s = input()[::-1]
d = 1
num = 0
ans = 0
mod_list = [0] * 2019
mod_list[0] = 1

for char in s:
    num += int(char) * d
    mod_list[num % 2019] += 1
    d *= 10
    d %= 2019

for i in range(2019):
    ans += mod_list[i] * (mod_list[i] - 1) //2

print(ans)
