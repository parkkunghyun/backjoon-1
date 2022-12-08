import sys
from collections import deque

sys.setrecursionlimit(30000)
input = sys.stdin.readline


def bfs(ans, node, check):
  que = deque([node])
  # print(que)
  while que:
    v = que.popleft()
    for i in ans[v]:
      if check[i] == -1:
        check[i] = check[v] + 1
        que.append(i)


city, road, info, start = map(int, input().split())
ans = [[] for _ in range(city + 1)]
check = [-1] * (city + 1)
check[start] = 0

for _ in range(road):
  a, b = map(int, input().split())
  ans[a].append(b)

#print(ans)
bfs(ans, start, check)

#print(check, "check")
if check.count(info):
  for i in range(len(check)):
    if check[i] == info:
      print(i, end=" ")
else:
  print(-1)
