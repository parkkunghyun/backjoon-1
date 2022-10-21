import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(input()))

cnt = 0
for i in range(n):
    pre = '/'
    for j in range(m):
        if arr[i][j] == '-':
            if arr[i][j] != pre:
                cnt += 1
        pre = arr[i][j]

for i in range(m):
    pre = '/'
    for j in range(n):
        if arr[j][i] == '|':
            if arr[j][i] != pre:
                cnt += 1
        pre = arr[j][i]
print(cnt)
