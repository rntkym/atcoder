s = list(input())
t = list(input())
change = len(t)

for i in range(len(s) - len(t) + 1):
    counter = 0
    for j, char in enumerate(s[i:i + len(t)]):
        if char == t[j]:
            counter += 1
    if change > (len(t) - counter):
        change = len(t) - counter

print(change)
