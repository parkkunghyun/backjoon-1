import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

a = [0] * 20000001
s = len(a) // 2
for i in range(n):
    z = l[i] + s
    a[z] += 1
k = []
for i in range(m):
    z = l2[i] + s
    print(a[z], end=" ")
