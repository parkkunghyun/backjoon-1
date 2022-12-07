import sys

sys.setrecursionlimit(30000)

input = sys.stdin.readline


def dfs(n):
  check[n] = True
  for i in ans[n]:
    if check[i] == False:
      check[i] = True
      dfs(i)


n, m = map(int, input().split())
ans = [[] for _ in range(n + 1)]
check = [False for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  ans[a].append(b)
  ans[b].append(a)

c = 0
for i in range(1, len(check)):
  if check[i] == False:
    c += 1
    dfs(i)

print(c)
