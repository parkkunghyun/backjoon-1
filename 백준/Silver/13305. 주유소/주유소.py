n = int(input())

load = list(map(int, input().split()))
liter = list(map(int, input().split()))
# 3 3 4
# 5 2 4 1
res = load[0] * liter[0]

m = liter[0]
dist = 0

for i in range(1,n-1):
    if liter[i] < m:
        res += m*dist 
        dist = load[i]
        m = liter[i]
    else:
        dist += load[i]
    if i == n-2:
        res += m*dist
print(res)