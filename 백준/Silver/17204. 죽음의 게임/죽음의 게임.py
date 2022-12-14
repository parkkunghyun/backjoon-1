import sys

sys.setrecursionlimit(30000)
input = sys.stdin.readline
from collections import deque
import itertools

n, bn = map(int, input().split())
l = [[] for _ in range(n)]
check = [0] * n

for i in range(n):
  a = int(input())
  l[i].append(a)

c = []


def dfs(x):
  if x == bn:
    c.append(check[x])
  for i in l[x]:
    if check[i] == 0:
      check[i] = check[x] + 1

      dfs(i)


dfs(0)
if check[bn] == 0:
  print(-1)
else:
  print(c[0])
