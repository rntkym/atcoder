import math

a, b, h, m = map(int, input().split())

angle_h = h * 30 + m * 0.5
angle_m = m * 6
diff = min(abs(angle_h - angle_m), 360 - abs(angle_h - angle_m))
cos = math.cos(math.radians(diff))
ans = a * a + b * b - 2 * a * b * cos

print(math.sqrt(ans))
