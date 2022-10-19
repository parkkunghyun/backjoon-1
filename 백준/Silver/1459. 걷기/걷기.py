x, y, w, s = map(int, input().split())

arr = []

m1 = (x + y) * w
m2 = 0
if (x + y) % 2 == 0:
    m2 = (max(x, y)) * s
else:
    m2 = (max(x, y) - 1) * s + w
m3 = (min(x, y) * s) + (abs(x - y) * w)
print(min(m1, m2, m3))
