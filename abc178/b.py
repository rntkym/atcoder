a, b, c, d =  map(int, input().split())
ans_list = [a * c, a * d, b * c, b * d]

print(max(ans_list))
