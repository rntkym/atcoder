n = int(input())
div_list = []

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        div_list.append(i)
        if i != n / i:
            div_list.append(n // i)
div_list.sort()
div_list = list(map(str, div_list))
print('\n'.join(div_list))
